var star_buttons = document.querySelectorAll(".star-button")

star_buttons.forEach(element => {
    element.addEventListener("click", function(){

        var idea_id = element.dataset.idea;
        var url = `http://${window.location.hostname}:${window.location.port}/star/${idea_id}`  
        fetch(url).then((response)=>{
            var response_data = response.json()
            console.log(response_data);
            if(response_data["success"] == "starred" || response_data["status"] == "unstarred"){
                element.classList.toggle("fa");
                element.classList.toggle("fas");
                element.classList.toggle("text-warning");

            }
        });
    });
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



function activate_navigation_link(linkto){
    links = document.querySelectorAll("#user-navigation-links > a")
    links.forEach(function(link){
        if(link.dataset.linkto == linkto){
            link.classList.toggle("active")
        }
    })
}


function activate_side_navigation_link(linkto){
    links = document.querySelectorAll("#user-side-navigation-links > a")
    links.forEach(function(link){
        if(link.dataset.linkto == linkto){
            link.classList.toggle("active")
        }
    })

}