const follow = document.querySelector('.follow-but')
const filt_sort_buts = document.querySelectorAll('.add-but')
const avatar_mini = document.querySelector('.user')
const sub_menu = document.querySelector('.sub-prof-menu')
const follow_block = document.querySelector('.follows-and-subs')
const buttons_follow = document.querySelectorAll('.follow-menu-but')
const cross_x = document.querySelector('.cross')


function toggle(trigg, targ, ad_class) {
    if (trigg && targ) {
        trigg.addEventListener('click', ()=>{
            targ.classList.toggle(ad_class)
            
        })   
    }
    else{
        return
    }
}

document.addEventListener('click', event=>{
    list_of_open_elems = document.querySelectorAll('.open')
    target_elem_cont = event.target.classList.contains('open')
    parent_elem_cont = event.target.parentNode.classList.contains('open')
    
    if (list_of_open_elems && !(parent_elem_cont || target_elem_cont) && !event.target.classList.contains('hidden')) {
        list_of_open_elems.forEach(elem=>{
            elem.classList.remove('open')
        })
    }
}, true)

toggle(avatar_mini, avatar_mini, 'open');

toggle(follow, follow, 'active')

filt_sort_buts.forEach(e=>{
    toggle(e, e, 'open')
})

buttons_follow.forEach(elem=>{
    toggle(elem, follow_block, 'active')
})

cross_x.addEventListener('click', ()=>{
    follow_block.classList.remove('active')
})