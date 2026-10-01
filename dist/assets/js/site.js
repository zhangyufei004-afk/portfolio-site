/* 全站脚本：仅用于增强体验，禁用 JS 时网站依然完全可用 */
(function () {
  "use strict";

  /* ---------------------------------------------- 移动端导航开合 */
  var toggle = document.querySelector(".navtoggle");
  var nav = document.getElementById("sitenav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------------------------------------------- 图片点击放大 */
  var box = document.createElement("div");
  box.className = "lightbox";
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-modal", "true");
  box.setAttribute("aria-label", "图片预览");
  box.innerHTML =
    '<button class="lightbox__close" type="button" aria-label="关闭预览">×</button>' +
    '<img class="lightbox__img" alt="">';
  document.body.appendChild(box);

  var boxImg = box.querySelector(".lightbox__img");

  function closeLightbox() {
    box.classList.remove("is-open");
    boxImg.removeAttribute("src");
  }

  document.addEventListener("click", function (e) {
    var img = e.target;
    if (img.tagName !== "IMG") return;
    if (img.closest(".card") || img.closest(".hero__cover")) return;
    boxImg.src = img.currentSrc || img.src;
    boxImg.alt = img.alt || "";
    box.classList.add("is-open");
  });

  box.addEventListener("click", function (e) {
    if (e.target === box || e.target.classList.contains("lightbox__close")) closeLightbox();
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeLightbox();
  });

  /* ---------------------------------------------- 目录高亮当前章节 */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc__list a"));
  if (!tocLinks.length || !("IntersectionObserver" in window)) return;

  var byId = {};
  var targets = [];
  tocLinks.forEach(function (a) {
    var id = decodeURIComponent(a.getAttribute("href").slice(1));
    var el = document.getElementById(id);
    if (el) {
      byId[id] = a;
      targets.push(el);
    }
  });

  var visible = {};
  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        visible[entry.target.id] = entry.isIntersecting ? entry.intersectionRatio : 0;
      });
      var bestId = null;
      var bestRatio = 0;
      Object.keys(visible).forEach(function (id) {
        if (visible[id] > bestRatio) {
          bestRatio = visible[id];
          bestId = id;
        }
      });
      tocLinks.forEach(function (a) {
        a.classList.remove("is-active");
      });
      if (bestId && byId[bestId]) byId[bestId].classList.add("is-active");
    },
    { rootMargin: "-84px 0px -55% 0px", threshold: [0, 0.25, 0.5, 0.75, 1] }
  );

  targets.forEach(function (el) {
    observer.observe(el);
  });
})();
