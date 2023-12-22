document.addEventListener("DOMContentLoaded", function() {
  let btn = document.getElementById('buyBtn');
  btn.addEventListener("click", get_session);
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
      else
        msg = `session_id = ${result.session_id}`
    } catch(err) {
      msg = err.toString();
    }
    alert(msg);
}