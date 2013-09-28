$(function () {
    $('#regist_user_tijiao').bind("click",function(){
    	var xmlhttp;
		if (window.XMLHttpRequest)
		{// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp=new XMLHttpRequest();
		}
		else
		{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
        xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				user_ID=document.getElementById("regist_user_ID").val();
				name = document.getElementById("regist_user_name").val();
				phone = document.getElementById("regist_user_phone").val();
				birth = document.getElementById("regist_user_birth".val();
				balance = document.getElementById("regist_user_balance").val();
			}
		}
		xmlhttp.open("POST","../regist_user/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		var postStr="user_ID="+user_ID+",name="+name+",phone="+phone+",birth="+birth;
		xmlhttp.send(postStr);
		$(#"message").text( "添加成功" ).show().fadeOut( 1000 );
    });
});
