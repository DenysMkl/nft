xhr = new XMLHttpRequest();
const url = window.location.href;
let data_of_users = undefined
const follow_count = document.querySelector('.followers-numb')
const follow_but = document.querySelector('.follow-but')
const show_follow_list = document.querySelectorAll('.follow-menu-but')
const swapp_item = document.querySelectorAll('.swapp-item')

if (follow_but){
    follow_but.addEventListener('click', ()=>{
        xhr.open('POST', url)
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        xhr.send(JSON.stringify({type:follow_but.dataset.act, process: follow_but.classList.contains('active') ? 'follow' : 'unfollow'}))
        xhr.onload = function() {
          try{
            data = JSON.parse(xhr.response);
            follow_count.textContent = data['followers_count']
          } catch (error){
            console.error('Error parsing stored data:', error);
         }
        }
      }
    )
}

show_follow_list.forEach(elem=>{
    elem.addEventListener('click', ()=>{
        xhr.open('POST', '/users_api');
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        xhr.send(JSON.stringify({type:elem.dataset.method, user_name: url.split('/').at(-1)}));
        xhr.onload = ()=>{
            try {
                data_of_users = JSON.parse(xhr.response)
                console.log(data_of_users)
            }
            catch(error) {
                console.error('Error parsing stored data:', error);
            }
            swapp_item.forEach(e=>{
                if (e.classList.contains('active')){
                    console.log(data_of_users[e.dataset.follow_type])
                }
            })
        }
    })
})

swapp_item.forEach(elem=>{
    elem.addEventListener('click', ()=>{
        console.log(data_of_users[elem.dataset.follow_type])
    })
})