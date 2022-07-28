//getting all html elemnets but filtering ones with class update-cart
var updateBtns = document.getElementsByClassName('update-cart')

for ( var i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
			var productId = this.dataset.product
			var action = this.dataset.action
			console.log('productId:', productId, 'action:', action)

			console.log('USER:', user)

			if (user === 'AnonymousUser'){
				addCookieItem(productId, action)
			}else{
				updateUserOrder(productId, action)
			}
	})
}

function updateUserOrder(productId, action){
		console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
				method:'POST',
				headers:{
					'Content-Type':'application/json',
					'X-CSRFToken':csrftoken,
				}, 
				body:JSON.stringify({'productId':productId, 'action':action})
		})
			

			.then((response) => {
					return response.json();
			})
			.then((data) => {
					console.log('data:', data)
					location.reload()
			})
			.catch((error)=> {
					console.log('error', error)
			})
	}

	function addCookieItem(productId, action){
	console.log('User is not authenticated')

		if (action == 'add'){
			if (cart[productId] == undefined){
			cart[productId] = {'quantity':1}

			}else{
				cart[productId]['quantity'] += 1
			}
		}

		if (action == 'remove'){
			cart[productId]['quantity'] -= 1

			if (cart[productId]['quantity'] <= 0){
				console.log('Item should be deleted')
				delete cart[productId];
			}
		}
		console.log('CART:', cart)
		document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

		location.reload()
		}

//function updateProductRating
//getting all html elemnets but filtering ones with class update-cart
var updateRating = document.getElementsByClassName('rating')

for ( var i = 0; i < updateRating.length; i++) {
	updateRating[i].addEventListener('click', function(){
			var productId = this.dataset.product
			var rating = this.dataset.value
			console.log('productId:', productId, 'rating:', rating)

			console.log('USER:', user)
	})
}

function updateProductRating(productId, rating){
	var url = '/productrating/'

	fetch(url, {

	method:'POST',
	headers:{
		'Content-Type':'application/json',
		'X-CSRFToken':csrftoken,
	}, 
	body1:JSON.stringify({'productId':productId, 'rating':rating})
})
			

		.then((response) => {
				return response.json();
		})
		.then((data) => {
				console.log('data:', data)
				location.reload()
		})
		.catch((error)=> {
				console.log('error', error)
		})
	}


	function processData(data) {
	var result = []
	dataset = JSON.parse(data);
	console.log(dataset)
	dataset.forEach(item => result.push(item.fields));
	return result;
	}

			$.ajax({
			url: $("#pivot-table-container").attr("send_data/"),
			dataType: 'json',
			success: function(data) {
					new Flexmonster({
							container: "#pivot-table-container",
							componentFolder: "https://cdn.flexmonster.com/",
							width: "100%",
							height: 430,
							toolbar: true,
							report: {
									dataSource: {
											type: "json",
											data: processData(data),
											mapping: {
											"Customer": {
													"caption": "Customer",
													"type": "model"
											},
											"Product": {
													"caption": "Products",
													"type": "model"
											},
											"Order": {
													"caption": "Order",
													"type": "model"
											},
									},
									},
									slice: {}
							}
					});
					new Flexmonster({
							container: "#pivot-chart-container",
							componentFolder: "https://cdn.flexmonster.com/",
							width: "100%",
							height: 430,
							//toolbar: true,
							report: {
									dataSource: {
											type: "json",
											data: processData(data),
											mapping: {
											"Customer": {
													"caption": "Customer",
													"type": "model"
											},
											"Product": {
													"caption": "Products",
													"type": "model"
											},
											"Order": {
													"caption": "Order",
													"type": "model"
											},
									},
									},
									
									slice: {},
									"options": {
											"viewType": "charts",
											"chart": {
													"type": "pie"
											}
									}
							}
					});
			}
	});
//diplaying dashboard if the user is Kelvin
document.addEventListener('DOMContentLoaded', function() {
	let dashboard = document.querySelector('.dashboard');
	if (user === 'Kelvin'){
		dashboard.style.visibility = "visible"
	}else{
		dashboard.style.visibility = "Hidded"
	}
})
if (user === 'kelvin'){
	d
}else{
	updateUserOrder(productId, action)
}