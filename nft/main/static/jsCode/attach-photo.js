const inp = document.querySelector('#user-bg');
const avatar = document.querySelector('#user-avatar');

inp.addEventListener('change', (event) => {
    const cur_bg_image = document.querySelector('.curr-user-bg');
    replace_image(cur_bg_image, inp)
});

avatar.addEventListener('change', (event) => {
    const cur_avatar_image = document.querySelector('.curr-user-avatar');
    replace_image(cur_avatar_image, avatar)
});

function replace_image(image_block, elem) {
    const file_of_img = new FileReader();
    file_of_img.readAsDataURL(elem.files[0]);
    file_of_img.addEventListener('load', () => {
        const url = file_of_img.result;
        image_block.src = url;
    });
}