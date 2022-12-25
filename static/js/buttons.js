const buttonLike = document.querySelector(".button_like");
const buttonDislike = document.querySelector(".button_dislike");
let likeIcon = document.querySelector(".icon_like");
let dislikeIcon = document.querySelector(".icon_dislike");
let count = document.querySelector("#count");
let countTwo = document.querySelector("#count-2");

let clicked = false;
let clickedTwo = false;

buttonLike.addEventListener("click", () => {
    if (!clicked) {
      clicked = true;
      likeIcon.innerHTML = `<img class="icon_like"</i>`
      count.textContent++;
    } else {
      clicked = false;
      likeIcon.innerHTML = `<img class="icon_like"</i>`
      count.textContent--;
    }
});

buttonDislike.addEventListener("click", () => {
    if (!clickedTwo) {
      clickedTwo = true;
      dislikeIcon.innerHTML = `<img class="icon_dislike"</i>`
      countTwo.textContent++;
    } else {
      clickedTwo = false;
      likeIcon.innerHTML = `<img class="icon_dislike"</i>`
      countTwo.textContent--;
    }
});

