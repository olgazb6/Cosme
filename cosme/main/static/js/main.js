$(document).ready(function(){
    var form = $("#f_buy");
    form.on('submit', function(e){
        e.preventDefault();
        
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('price');
        console.log(product_id);
        console.log(product_name);
    })
    
});
