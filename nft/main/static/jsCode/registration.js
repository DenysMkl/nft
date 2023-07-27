labels = gsap.utils.toArray('.lab')
inputTags = gsap.utils.toArray('.inputTag')
but = document.querySelector('#create')
userName = document.querySelector('#fullName')
userMail = document.querySelector('#email')
passArea = document.querySelectorAll('.pass')
let [password, repeatpass] = passArea
showPassIcons = gsap.utils.toArray('.fa-eye-slash')
inputBlock = gsap.utils.toArray('.inputBlock')
checkBut = document.querySelector('.checkboxFake')

inputTags.forEach((elem)=>{
    elem.addEventListener('focus', ()=>{
        labels[inputTags.indexOf(elem)].classList.add('active')
    })
    elem.addEventListener('blur', ()=>{
        if (elem.value.trim() == '') {
            labels[inputTags.indexOf(elem)].classList.remove('active')
        }
    })
})


showPassIcons.forEach(elem=>{
    elem.addEventListener('click', ()=>{

        if (elem.classList.contains('fa-eye-slash')) {
            elem.classList.replace('fa-eye-slash', 'fa-eye')
            passArea[showPassIcons.indexOf(elem)].type = 'text'
        }
        else {
            elem.classList.replace('fa-eye', 'fa-eye-slash')
            passArea[showPassIcons.indexOf(elem)].type = 'password'
        }
    })
})

checkBut.addEventListener('click', ()=>{
    checkBut.classList.toggle('active')
})

gsap.from('.form-areas', {
    opacity: 0,
    duration: 1,
    translateY: '-100px'
})