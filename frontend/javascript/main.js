const keyMap={
   'a':'btn-a',
   'b':'btn-b',
   'c':'btn-c',
   'd':'btn-d',
   'e':'btn-e',
   'f':'btn-f',
   'g':'btn-g',
   'h':'btn-h',
   'i':'btn-i',
   'j':'btn-j',
   'k':'btn-k',
   'l':'btn-l',
   'm':'btn-m',
   'n':'btn-n',
   'o':'btn-o',
   'p':'btn-p',
   'q':'btn-q',
   'r':'btn-r',
   's':'btn-s',
   't':'btn-t',
   'u':'btn-u',
   'v':'btn-v',
   'w':'btn-w',
   'x':'btn-x',
   'y':'btn-y',
   'z':'btn-z',
};
window.addEventListener("keydown",(event)=>{
   const key=event.key.toLowercase();
   if (keyMap[key]) {
      const buttonId=keyMap[key];
      const button=document.getElementById(buttonId)

      if (button){
         button.onclick();
      }
   }
});

if (button) {
    button.classList.add('active-press');
    button.click();
    
    setTimeout(() => {
        button.classList.remove('active-press');
    }, 100);
}