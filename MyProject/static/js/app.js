const text = document.querySelector(".fancy");
const StrText = text.textContent;
const SplitText = StrText.split("");

text.textContent = "";

for(let i=0; i < SplitText.length; i++){
  text.innerHTML += "<span>" + SplitText[i] + "</span>";
}

let char = 0;
let timer = setInterval(onTick, 50);

function onTick(){
  const span = text.querySelectorAll("span")[char];
  span.classList.add("fade");
  char++;
  if(char === SplitText.length){
    complete();
    return;
  }
}

function complete(){
  clearInterval(timer);
  timer = null;
}
