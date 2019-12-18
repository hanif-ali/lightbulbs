var star_buttons = document.querySelectorAll(".star-button")

star_buttons.forEach(element => {
    element.addEventListener("click", function(){

        var idea_id = element.dataset.idea;
        var url = `http://${window.location.hostname}:${window.location.port}/star/${idea_id}`  
        fetch(url).then(res => res.json())
                .then(data => {
                    if(data["status"] == "starred"){
                        element.classList.add("fa");
                        element.classList.add("fas");
                        element.classList.add("text-warning");
                    }
                    else if (data["status"] == "unstarred"){
                        element.classList.remove("fa");
                        element.classList.remove("fas");
                        element.classList.remove("text-warning");

                    }
                })
            })
});

var upvote_buttons = document.querySelectorAll(".upvote-button")

upvote_buttons.forEach(element => {
    element.addEventListener("click", function(){
        var idea_id = element.dataset.idea;
        var url = `http://${window.location.hostname}:${window.location.port}/upvote/${idea_id}`  
        fetch(url).then(res => res.json())
                .then(data => {
                    if(data["status"] == "upvoted"){
                        element.classList.add("text-warning")
                    }

                    else if (data["status"] == "unupvoted"){
                        element.classList.remove("text-warning")

                    }
                })
            })
})

var downvote_buttons = document.querySelectorAll(".downvote-button")

downvote_buttons.forEach(element => {
    element.addEventListener("click", function(){
        var idea_id = element.dataset.idea;
        var url = `http://${window.location.hostname}:${window.location.port}/downvote/${idea_id}`  
        fetch(url).then(res => res.json())
                .then(data => {
                    if(data["status"] == "downvoted"){
                        element.classList.add("text-warning")
                    }

                    else if (data["status"] == "undownvoted"){
                        element.classList.remove("text-warning")

                    }
                })
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