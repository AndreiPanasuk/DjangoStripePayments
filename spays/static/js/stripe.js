$(document).ready(function(){
    $("#buyBtn").on("click",function(event){
        let id = document.getElementById('#pk').value;  
        let count = document.getElementById('#count').value;
        let url = `/buy/${id}/?count=${count}`;
        fetch({
          url: "/buy",            
          method: "GET",
          success: function(data){
              console.log(data);
          },
          error: function(){
            alert("error");
          }
        });
    });
});