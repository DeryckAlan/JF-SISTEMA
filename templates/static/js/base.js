let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#sb-menu-btn");
let outside = document.querySelector(".home-section")

closeBtn.addEventListener("click", ()=>{
    toggleSidebar();
    toggleHomeSection();
});

// outside.addEventListener("click", ()=>{
    // if(sidebar.classList.contains("open")){
        // toggleSidebar();
        // toggleHomeSection();
    // };
// });

function toggleSidebar() {
    sidebar.classList.toggle("open");

}

function toggleHomeSection() {

    if(sidebar.classList.contains("open")){
        outside.style.left = '250px';
        outside.setProperty('width', 'calc(100% - 250px)');
    }else {
        outside.style.left = '78px';
        outside.setProperty('width', 'calc(100% - 78px)');
    }

}
