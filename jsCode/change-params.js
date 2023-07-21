const filt_and_sort_blocks = document.querySelectorAll('.hidden-menu-block')


filt_and_sort_blocks.forEach(elem=>{
    const hidden_elems = elem.querySelectorAll('.hidden-menu-item')
    
    elem.addEventListener('click', event=>{
        closest_item = event.target.closest('.hidden-menu-item')

        hidden_elems.forEach(element=>{
            if (closest_item){
                element.classList.toggle('active', closest_item == element)
            }
        })
    })
})