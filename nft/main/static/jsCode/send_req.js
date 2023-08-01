xhr = new XMLHttpRequest();

document.addEventListener('click', ()=>{
    xhr.open('POST', '/api_u')
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({data:'Hello world'}))
    xhr.onload = ()=>{
        console.log('it works')
    }
})