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


var notification_delete_buttons = document.querySelectorAll(".notification-delete")
notification_delete_buttons.forEach(button => {
    button.addEventListener('click', (event)=>{

        var notification_id = button.dataset.notification;
        var url = `http://${window.location.hostname}:${window.location.port}/notifications/delete/${notification_id}`  
        fetch(url).then(res => res.json())
                .then(data => {
                    if(data["success"]){
                        alert_div = button.parentElement
                        alert_div.remove()
                    }
                })
            })
    })


var message_delete_buttons = document.querySelectorAll(".message-delete")
message_delete_buttons.forEach(button => {
    button.addEventListener('click', event => {
        message_id = button.dataset.message
        confirmation = confirm("Do you want to delete this message?")
        if(confirmation){
            document.location.replace(`http://${window.location.hostname}:${window.location.port}/inbox/delete/${message_id}`)
        }
    })
})


var proposal_delete_buttons = document.querySelectorAll(".sent-delete")

proposal_delete_buttons.forEach(button => {
    button.addEventListener('click', event => {
        proposal_id = button.dataset.proposal
        confirmation = confirm("Are you sure you want to delete the sent proposal?")
        if(confirmation){
            document.location.replace(`http://${window.location.hostname}:${window.location.port}/me/sent/delete/${proposal_id}`)
        }
    })
})



var created_delete_buttons = document.querySelectorAll(".created-delete-button")
created_delete_buttons.forEach(button => {
    button.addEventListener('click', event => {
        idea_id = button.dataset.idea;
        confirmation = confirm("Are you sure you want to delete the Idea?")
        if(confirmation){
            document.location.replace(`http://${window.location.hostname}:${window.location.port}/me/ideas/delete/${idea_id}`)
        }
    })
})