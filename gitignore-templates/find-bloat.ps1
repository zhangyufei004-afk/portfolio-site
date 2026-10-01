# ============================================================================
#  找出仓库里「占体积的元凶」（本地运行，需要先 clone）
#
#  用法：
#      1. git clone https://github.com/zhangyufei004-afk/Instance-43.git
#      2. cd Instance-43
#      3. 把本文件另存为 find-bloat.ps1，然后执行：
#             powershell -ExecutionPolicy Bypass -File find-bloat.ps1
#
#  它会报告两件事：
#      A. .git 目录有多大（= 历史体积，删文件不会减小它）
#      B. 历史上最大的 20 个对象 —— 这些才是真正占地方的东西
# ============================================================================

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".git")) {
    Write-Host "当前目录不是 git 仓库。先 clone 再运行。" -ForegroundColor Red
    exit 1
}

$repoName = Split-Path -Leaf (Get-Location)

Write-Host "==================== $repoName ====================" -ForegroundColor Cyan
Write-Host ""

# ---------- A. .git 目录大小 ----------
$gitSize = (Get-ChildItem ".git" -Recurse -File -Force -ErrorAction SilentlyContinue |
            Measure-Object -Property Length -Sum).Sum
Write-Host ("A. .git 目录大小: {0:N1} MB  (这部分是历史，删文件不会变小)" -f ($gitSize / 1MB)) -ForegroundColor Yellow
Write-Host ""

# ---------- B. 历史里最大的对象 ----------
Write-Host "B. 历史中最大的 20 个对象：" -ForegroundColor Yellow

$packDir = ".git\objects\pack"
if (-not (Test-Path $packDir)) {
    Write-Host "   没有 pack 文件（仓库很小或未打包）"
    exit 0
}

$idxFiles = Get-ChildItem $packDir -Filter "*.idx"
if (-not $idxFiles) {
    Write-Host "   没有 .idx 文件"
    exit 0
}

$lines = @()
foreach ($idx in $idxFiles) {
    # verify-pack 会输出：SHA1 type size size-in-packfile offset-in-packfile
    $out = & git verify-pack -v $idx.FullName 2>$null
    foreach ($l in $out) {
        # 只看 blob（文件内容），跳过 commit/tree/delta 行
        if ($l -match '^([0-9a-f]{40})\s+blob\s+(\d+)\s+(\d+)') {
            $lines += [pscustomobject]@{
                Sha   = $Matches[1]
                Size  = [int64]$Matches[2]
            }
        }
    }
}

$top = $lines | Sort-Object Size -Descending | Select-Object -First 20

if (-not $top) {
    Write-Host "   未找到 blob 对象"
    exit 0
}

Write-Host ""
Write-Host ("   {0,-10} {1,-12} {2}" -f "大小", "SHA(短)", "文件路径（可能已从工作区删除）")
Write-Host ("   {0,-10} {1,-12} {2}" -f "--------", "-----------", "----------------------------")

foreach ($o in $top) {
    $path = (& git rev-list --objects --all 2>$null |
             Select-String -Pattern "^$($o.Sha)\s" |
             Select-Object -First 1) -replace "^$($o.Sha)\s+", ""
    if (-not $path) { $path = "(无法定位 / 可能是旧版本的文件内容)" }
    $mb = $o.Size / 1MB
    $flag = if ($mb -ge 5) { "  <== 重点" } else { "" }
    Write-Host ("   {0,-10} {1,-12} {2}{3}" -f ("{0:N2} MB" -f $mb), $o.Sha.Substring(0,10), $path, $flag)
}

# ---------- C. 建议 ----------
Write-Host ""
Write-Host "C. 结论与建议：" -ForegroundColor Green
$big = ($top | Where-Object { $_.Size -ge 5MB }).Count
if ($big -gt 0) {
    Write-Host "   有 $big 个超过 5MB 的历史对象。想彻底瘦身需要改写历史（git filter-repo），"
    Write-Host "   或者更省事的做法：新建一个干净仓库，只提交当前需要的内容。"
} else {
    Write-Host "   历史里没有特别大的单个对象，体积可能来自大量中等文件的历史累积。"
}
Write-Host ""
Write-Host "   工作区当前各目录大小（对照用）：" -ForegroundColor Gray
Get-ChildItem -Directory -Force |
    Where-Object { $_.Name -ne ".git" } |
    ForEach-Object {
        $s = (Get-ChildItem $_.FullName -Recurse -File -Force -ErrorAction SilentlyContinue |
              Measure-Object -Property Length -Sum).Sum
        if ($s -gt 1MB) { Write-Host ("     {0,-24} {1,8:N1} MB" -f $_.Name, ($s / 1MB)) }
    }
