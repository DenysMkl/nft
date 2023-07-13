
const bounce = document.querySelector('.add-info-block')
const line = document.querySelector('.active-line')
const list_block = document.querySelector('.add-info-nav')

list_block.addEventListener('click', event=>{
    list_items = Array.from(list_block.children)

    check = event.target.closest('.add-info-item')

    if (check){
        list_items.forEach(elem => {
            elem.classList.toggle('active', check == elem)
        });
    }
    var rect = check.getBoundingClientRect()
    var rect_bounce = bounce.getBoundingClientRect()
    line.style.transform = `translateX(${rect.x - rect_bounce.x}px)`
    line.style.width = `${check.offsetWidth}px`
})