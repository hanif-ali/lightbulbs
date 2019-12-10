var star_buttons = document.querySelectorAll(".star-button")

star_buttons.forEach(element => {
    element.addEventListener("click", function(){
        // Do some Star Logic
        element.classList.toggle("fa");
        element.classList.toggle("fas");
        element.classList.toggle("text-warning");
    })
});

var upvote_buttons = document.querySelectorAll(".upvote-button")

upvote_buttons.forEach(element => {
    element.addEventListener("click", function(){
        // Do some upvote logic
        element.classList.toggle("text-warning")
    })
})

var downvote_buttons = document.querySelectorAll(".downvote-button")

downvote_buttons.forEach(element => {
    element.addEventListener("click", function(){
        // Do some upvote logic
        element.classList.toggle("text-warning")
    })
})