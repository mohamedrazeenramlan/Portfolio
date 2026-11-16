const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector("#site-nav");

toggle.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", String(open));
  toggle.textContent = open ? "Close" : "Menu";
});

nav.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    nav.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.textContent = "Menu";
  });
});

const dialog = document.querySelector("#lightbox");
const dialogImg = dialog.querySelector("img");

document.querySelectorAll(".collage button, .patent img, .awards img").forEach((node) => {
  node.addEventListener("click", () => {
    const source = node.dataset.full || node.currentSrc || node.src;
    const img = node.querySelector("img") || node;
    dialogImg.src = source;
    dialogImg.alt = img.alt || "Project image";
    dialog.showModal();
  });
});

dialog.addEventListener("click", (event) => {
  if (event.target === dialog) dialog.close();
});

dialog.addEventListener("close", () => {
  dialogImg.src = "";
});
