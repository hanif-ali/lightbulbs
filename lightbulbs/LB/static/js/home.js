function activate_navigation_link(linkto){
    links = document.querySelectorAll("#navigation-links > a")
    links.forEach(function(link){
        if(link.dataset.linkto == linkto){
            link.classList.toggle("active")
        }
    })
}