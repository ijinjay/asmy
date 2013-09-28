$(function () {
    $('#regist_designer_tijiao').bind("click",function(){
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
				designer_ID=document.getElementById("regist_designer_ID").val();
				name = document.getElementById("regist_designer_name").val();
				phone = document.getElementById("regist_designer_phone").val();
				birth = document.getElementById("regist_designer_birth").val();
			}
		}
		xmlhttp.open("POST","../regist_designer/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		var postStr=["designer_id":user_id,"name":name,"phone":phone,"birth":birth];
		xmlhttp.send(postStr);
		$(#"message").text( "添加成功" ).show().fadeOut( 1000 );
    });
});
