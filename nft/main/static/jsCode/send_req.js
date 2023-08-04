xhr = new XMLHttpRequest();
url = window.location.href;

follow_but = document.querySelector('.follow-but')

follow_but.addEventListener('click', ()=>{
    xhr.open('POST', url)
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({type:follow_but.dataset.act, process: follow_but.classList.contains('active') ? 'follow' : 'unfollow'}))
    xhr.onload = ()=>{
        console.log('it works')
    }
    xhr.onload = function() {
      try{
        data = JSON.parse(xhr.response);
      } catch (error){
        console.error('Error parsing stored data:', error);
     }
     console.log(data)
    }
  }
)