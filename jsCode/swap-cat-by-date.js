parent = document.querySelector('.sort-by-date')

parent.addEventListener('click', (event)=>{
    
    elements = Array.from(parent.children)
    targetElem = event.target.closest('.sort-by-date .but')
    if (targetElem){
        elements.forEach(elem => {
            elem.classList.toggle('active', targetElem == elem)
        });
    }
})