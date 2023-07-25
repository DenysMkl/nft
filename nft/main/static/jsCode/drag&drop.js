const drop_area = document.querySelector('.drop-new-img')
const input_area_for_nft = document.getElementById('upl-nft')
lab = document.querySelector('.label-drop label span')


drop_area.addEventListener('dragover', dragOverHandler);
drop_area.addEventListener('drop', dropHandler);

input_area_for_nft.addEventListener('change', ()=>{
    lab.textContent = input_area_for_nft.value.split(`\\`).at(-1)
})

function dragOverHandler(event) {
    event.preventDefault();
}


function dropHandler(event) {
    event.preventDefault();
    const files = event.dataTransfer.files;
    input_area_for_nft.files = files;
    lab.textContent = input_area_for_nft.value.split(`\\`).at(-1)
}