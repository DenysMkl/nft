const bounce = document.querySelectorAll('.add-info-block')
const line = document.querySelectorAll('.active-line')
const list_block = Array.from(document.querySelectorAll('.add-info-nav'))
const list_items =  list_block.map(elem=>Array.from(elem.children))
const buttons_follow = Array.from(document.querySelectorAll('.follow-menu-but'))
const follow_block = document.querySelector('.follows-and-subs')
const cross_x = document.querySelector('.cross')
const swapper_items = Array.from(document.querySelectorAll('.swapp-item'))

function position_line(bounce, line, list_block, list_items){
    active_elem = list_items.filter(elem=>elem.classList.contains('active'))[0]
    line.style.left = `${active_elem.getBoundingClientRect().x - bounce.getBoundingClientRect().x}px`
    line.style.width = `${active_elem.offsetWidth}px`
    line.style.transform = `translateX(0px)`

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
}


buttons_follow.forEach(elem=>{
    elem.addEventListener('click', ()=>{
        follow_block.classList.add('active')
        swapper_items.forEach(e=>{
            e.classList.remove('active')
        })
        swapper_items[buttons_follow.indexOf(elem)].classList.add('active')
        position_line(bounce[0], line[0], list_block[0], list_items[0])
    })
})

cross_x.addEventListener('click', ()=>{
    follow_block.classList.remove('active')
    swapper_items.forEach(e=>{
        e.classList.remove('active')
    })
})

position_line(bounce[1], line[1], list_block[1], list_items[1])
position_line(bounce[0], line[0], list_block[0], list_items[0])