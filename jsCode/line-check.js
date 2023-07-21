
const bounce = document.querySelector('.add-info-block')
const line = document.querySelector('.active-line')
const list_block = document.querySelector('.add-info-nav')
const list_items = Array.from(list_block.children)

line.style.left = `${list_items[0].getBoundingClientRect().x - bounce.getBoundingClientRect().x}px`
line.style.width = `${list_items[0].offsetWidth}px`

list_block.addEventListener('click', event=>{
    check = event.target.closest('.add-info-item')
    if (check){
        line.style.left = `0px`
        list_items.forEach(elem => {
            elem.classList.toggle('active', check == elem)
        });
        var rect = check.getBoundingClientRect()
        var rect_bounce = bounce.getBoundingClientRect()
        line.style.transform = `translateX(${rect.x - rect_bounce.x}px)`
        line.style.width = `${check.offsetWidth}px`
    }
})