avatar = document.querySelector('.user')
sub_menu = document.querySelector('.sub-prof-menu')

avatar.addEventListener('click', ()=>{
    sub_menu.classList.toggle('active')
})