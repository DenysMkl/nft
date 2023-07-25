var cap = 30

const items = document.querySelectorAll('.marketblock')
const show_more = document.querySelectorAll('.show-card')


// Создание родительского элемента <div class="nft-card">
var nftCard = document.createElement('div');
nftCard.className = 'nft-card';

// Создание элемента <div class="image-block">
var imageBlock = document.createElement('div');
imageBlock.className = 'image-block';

// Создание элемента <img src="./photos/nftcard.png" alt="nft-card" class="nft-img">
var img = document.createElement('img');
img.src = './photos/nftcard.png';
img.alt = 'nft-card';
img.className = 'nft-img';

// Добавление <img> внутрь <div class="image-block">
imageBlock.appendChild(img);

// Создание элемента <span class="nft-name">azuki 3D</span>
var nftName = document.createElement('span');
nftName.className = 'nft-name';
nftName.textContent = 'azuki 3D';

// Создание горизонтальной линии <hr>
var hr = document.createElement('hr');

// Создание блока для покупки <div class="buy-block">
var buyBlock = document.createElement('div');
buyBlock.className = 'buy-block';

// Создание элемента <span class="price">0.4000 ETH</span>
var price = document.createElement('span');
price.className = 'price';
price.textContent = '0.4000 ETH';

// Создание ссылки <a href="#" class="but buy-but">buy now</a>
var buyLink = document.createElement('a');
buyLink.href = '#';
buyLink.className = 'but buy-but';
buyLink.textContent = 'buy now';

// Добавление <span> и <a> внутрь <div class="buy-block">
buyBlock.appendChild(price);
buyBlock.appendChild(buyLink);

// Добавление всех элементов внутрь родительского элемента <div class="nft-card">
nftCard.appendChild(imageBlock);
nftCard.appendChild(nftName);
nftCard.appendChild(hr);
nftCard.appendChild(buyBlock);

// Добавление готового блока в определенное место на странице, например, внутрь элемента с id "container"

items[0].insertBefore(nftCard, show_more[0]);


