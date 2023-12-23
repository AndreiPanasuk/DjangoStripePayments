document.addEventListener("DOMContentLoaded", function() {
  let btn = document.getElementById('buyBtn');
  if (btn)
    btn.addEventListener("click", get_session);
  let btnOrder = document.getElementById('buyOrderBtn');
  if (btnOrder)
    btnOrder.addEventListener("click", get_order_session);
});
async function get_session(event) {
    let id = parseInt(document.getElementById('pk').value); 
    if (!id) return alert('ERROR: product ID not found'); 
    let count = parseInt(document.getElementById('count').value);
    if (!(count>0)) return alert(`ERROR: bad product count ${count}`); 
    let url = `/buy/${id}/?count=${count}`;
    let response = await fetch(url);
    let msg;
    try {
      let result = await response.json();
      console.log(result);
      if (result.error)
        msg = `ERROR: ${result.error}`
      else {
        msg = `session_id = ${result.session_id}`;
        console.log(msg)
        window.open(result.session_url, "PaymentTab");
      }
    } catch(err) {
      msg = err.toString();
    }
    alert(msg);
}
async function get_order_session(event) {
    let csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value; //getCookie('csrftoken');
    let elments = document.getElementsByClassName('count')
    let items = [];
    for(let elm of elments){
      let count = parseInt(elm.value);
      if (count<0) return alert(`ERROR: bad product count ${count}`); 
      if (count) {
        let id = parseInt(elm.getAttribute('product_id')); 
        items.push({id, count})
      }
    }
    if (!items.length) return alert('ERROR: set the count of products'); 
    let data = {products: items}
    let url = `/buy/order/`;
    let response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': csrftoken,
        'credentials': 'include',
      },
      body: JSON.stringify(data)
    });
    let msg;
    try {
      let result = await response.json();
      console.log(result);
      if (result.error)
        msg = `ERROR: ${result.error}`
      else {
        msg = `session_id = ${result.session_id}`;
        console.log(msg)
        window.open(result.session_url, "PaymentTab");
      }
    } catch(err) {
      msg = err.toString();
    }
    alert(msg);
}