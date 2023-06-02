const text = document.querySelector(".sec-text");

const textLoad = () => {
  setTimeout(() => {
    text.textContent = "Étudiante📖";
  }, 0);
  setTimeout(() => {
    text.textContent = "Développeuse💻";
  }, 4000);
  setTimeout(() => {
    text.textContent = "Passionnée🤩";
  }, 8000); //1s = 1000 milliseconds
};

textLoad();
setInterval(textLoad, 12000);
