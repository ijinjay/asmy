var xmlhttp;
if (window.XMLHttpRequest)
{// code for IE7+, Firefox, Chrome, Opera, Safari
	xmlhttp=new XMLHttpRequest();
}
else
{// code for IE6, IE5
	xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
$(function () {
    $('#myField').bind("click",function(){
        xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				c=document.getElementById("test");
				c.style.display='block';
				c.innerHTML=xmlhttp.responseText;
			}
		}
		xmlhttp.open("GET","../hello",true);
		xmlhttp.send();
    });
});
