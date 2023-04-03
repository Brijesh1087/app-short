$(document).ready(()=> {
	const load = (len) => {
		let container = document.querySelector(".main .root");
		// let desc = "Lorem hello python ..."
		for(let x=1;x<=len;x++){
			let url = `https://jsonplaceholder.typicode.com/posts/${Math.floor(Math.random()*90)}`
			fetch(url).then(res=>res.json()).then(data=> {
				let card = document.createElement('div');
				let height = Math.floor(Math.random()* (300 - 250 + 1) + 250);
				let width = Math.floor(Math.random()* (300 - 250 + 1) + 250);
				card.classList.add('card');
				card.classList.add('rounded')
				card.style.backgroundImage = `url(https://source.unsplash.com/random/500x${height})`;
				card.style.height = `${height}px`;
				card.innerHTML = `
				<div class="time">
					<span class='p-1  rounded bg-white text-dark'>${Math.floor(Math.random()*60)}:${Math.floor(Math.random()*60)}</span>
				</div>
				<div class='play'>
					<ion-icon name="play-circle-outline" class='icon'></ion-icon>
				</div>
				<div class="info">
					<span class="desc">${data.title.slice(0, Math.floor(Math.random()* (70 -20 + 1) + 20))}...</span>
					<div class="profile">
						<img src="https://source.unsplash.com/random/${Math.floor(Math.random()*300)}:${Math.floor(Math.random()*600)}" class="img-fluid">
						<b class="username">tanaypratap</b>
					</div>
				</div>
				`;
			container.appendChild(card)
			})
		}
	}
	load(5)
	let loading = false;
	let page = 0;
	 window.addEventListener('scroll',()=> {
	 	let {scrollTop, scrollHeight, clientHeight} = document.documentElement;
	 	if(scrollTop + clientHeight >= scrollHeight - 300  && !loading){
	 		loading = true;
	 		load(2)
	 		loading = false;
	 		page += 1
	 		console.log(page)
	 	}
	 })
})
