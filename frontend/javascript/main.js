document.addEventListener("DOMContentLoaded",()=>{
const btn=document.getElementById("start_button");
btn.addEventListener("click",() => {
    console.log("Clicked!");
});
fetch("http://127.0.0.1:8000/games")
.then(response => response.json())
.then(data =>{

}

)

});