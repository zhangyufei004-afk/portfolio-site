"""
发布构建脚本 —— 供静态托管平台（帽子云 / EdgeOne Pages 等）调用。

背景：本仓库的站点由 `build.py` 在本地生成，产物已提交在 `dist/`。
托管平台不认识 Python，但如果把 `dist/` 的内容再复制一份到平台约定的输出目录
（通常是仓库根的 `public/`），无论平台把"输出目录"理解成 `dist` 还是 `public`，
都能拿到完整站点。

本地生成站点仍然只跑 `python build.py`，这个脚本只服务于云端部署。
"""
import os
import shutil
import sys

SITE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(SITE, "dist")
DST = os.path.join(SITE, "public")


def main():
    if not os.path.isdir(SRC):
        sys.stderr.write("[build_for_host] 找不到 dist/，请先在本地运行 python build.py\n")
        return 1

    # 重新生成一份 public/，避免残留旧文件
    if os.path.isdir(DST):
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)

    # 统计结果，便于在平台日志里确认真的复制成功了
    files = 0
    total = 0
    for root, _dirs, names in os.walk(DST):
        for n in names:
            files += 1
            total += os.path.getsize(os.path.join(root, n))

    print("[build_for_host] dist/ -> public/ 完成")
    print("[build_for_host] 文件数 %d，合计 %.1f MB" % (files, total / 1024 / 1024))
    print("[build_for_host] 请把平台的输出目录设为 public（若填 dist 也可，两者内容一致）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
