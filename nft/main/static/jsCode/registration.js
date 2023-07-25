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


function validPassword(pass){
    return pass.value.trim().length >= 8
}


function validRepeatPass(pass, rep) {
    return rep.value == pass.value && rep.value.trim().length >= 8
}


function validName(fullName) {
    return fullName.value.trim() != '' && fullName.value.trim().split(' ').length == 2
}


function validEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return re.test(email.value)
}


function allValid() {
    allConfirm = [validName(userName), validEmail(email), validPassword(password), validRepeatPass(password, repeatpass)].every((param)=>param == true)
    if (allConfirm &&  checkBut.classList.contains('active')){
        but.classList.add('active')
        but.disabled = false
    }
    else{
        but.classList.remove('active')
        but.disabled = true
    }
}


function playAnimation(block) {
    gsap.from(block, {
        translateX: '10px',
        duration: .1,
        repeat: 4,
        yoyo: true,
    })
}


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


inputTags.forEach(tag=>{
    tag.addEventListener('blur', ()=>{
        boolValue = null
        switch (tag.name) {
            case 'fullName':
                boolValue = validName(tag)
                break

            case 'mail':
                boolValue = validEmail(tag)  
                break

            case 'pass':
                boolValue = validPassword(password)
                break

            case 'repeatpass':
                boolValue = validRepeatPass(password,repeatpass)
                break

            default:
                break
        }
        if (!boolValue) {
            playAnimation(inputBlock[inputTags.indexOf(tag)])
        }
        allValid()

    })
})


checkBut.addEventListener('click', ()=>{
    checkBut.classList.toggle('active')
    allValid()
})

gsap.from('.form-areas', {
    opacity: 0,
    duration: 1,
    translateY: '-100px'
})