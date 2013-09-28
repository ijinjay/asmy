function createRequest() {
	try {
		request = new XMLHttpRequest();
	} 
	catch (tryMS) {
		try {
			request = new ActiveXObject("Msxml2.XMLHTTP");
		} 
		catch (otherMS) {
			try {
			    request = new ActiveXObject("Microsoft.XMLHTTP");
			} 
			catch (failed) {
			    request = null;
		  }
		}
	}
	return request;
}
// function track the query
function query_button (xmlhttp) {
    $('#query').bind("click",function(){
    	var user_id = $('#user_id').val();
    	$('#result').show();
        xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				x=document.getElementById("result");
				x.style.visibility="visible";	
				x.innerHTML=xmlhttp.responseText;
			}
		}
		xmlhttp.open("POST","../query/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		var postStr="user_id="+user_id;
		xmlhttp.send(postStr);
    });
};

function non_vip(xmlhttp){
	$('#non_submit').bind("click",function(){
		money = document.getElementById("non_money").value;
		designer_ID = document.getElementById("non_designer_ID").value;
		type = document.getElementById("non_type").value;
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				x=document.getElementById("messagebox");
				$("#messagebox").show();
				x.innerHTML=xmlhttp.responseText;
				$("#messagebox").fadeOut(8000);
			}
		}
		xmlhttp.open("POST","../non_vip/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		var postStr = "money="+money+"&designer_ID="+designer_ID+"&type="+type;
		xmlhttp.send(postStr);
	});
};
function clean_button (){
	$('#clean').bind("click",function(){
		$('#result').hide();
	});
};
function vip(xmlhttp){
	$('#vip_submit').bind("click",function(){
		user_id = $('#user_id').val();
		money = document.getElementById("vip_money").value;
		designer_ID = document.getElementById("vip_designer_ID").value;
		type = document.getElementById("vip_type").value;
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				x=document.getElementById("messagebox");
				$("#messagebox").show();
				x.innerHTML=xmlhttp.responseText;
				$("#messagebox").fadeOut(8000);
			}
		}
		xmlhttp.open("POST","../vip_consume/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		var postStr = "user_id="+user_id+"&money="+money+"&designer_ID="+designer_ID+"&type="+type;
		xmlhttp.send(postStr);
	})
}
function add_money(xmlhttp){
	$("#add_money").bind("click",function(){
		money = $('#inputAddMoney').val();
		user_id = $('#user_id').val();
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				x=document.getElementById("messagebox");
				$("#messagebox").show();
				x.innerHTML=xmlhttp.responseText;
				$("#messagebox").fadeOut(8000);
			}
		}
		xmlhttp.open("POST","../add_money/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		var postStr = "user_id="+user_id+"&money="+money;
		xmlhttp.send(postStr);
	})
}
function regist_VIP(xmlhttp){
	$('#regist_vip').bind("click",function(){
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				x=document.getElementById("messagebox2");
				$("#regist_user_box").show();
				$("#messagebox2").show();
				y = document.getElementById("regist_user_box");
				y.style.display ="block";
				// x.innerHTML=xmlhttp.responseText;
			}
		}
		xmlhttp.open("POST","../regist_user_page/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		xmlhttp.send("");
	});
};
function regist_Designer(xmlhttp){
	$('#regist_designer').bind("click",function(){
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				x=document.getElementById("messagebox3");
				$("#regist_designer_box").show();
				$("#messagebox3").show();
				y = document.getElementById("regist_designer_box");
			}
		}
		xmlhttp.open("POST","../regist_designer_page/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		xmlhttp.send("");
	});
};
function regist_VIP_result(xmlhttp){
	$("#regist_user_tijiao").bind("click",function(){
		user_id = $('#regist_user_ID').val();
		name = $('#regist_user_name').val();
		phone = $('#regist_user_phone').val();
		birth = $('#regist_user_birth').val();
		balance = $('#regist_user_balance').val();
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				y = document.getElementById("regist_user_box");
				y.style.display ="none";
				$('#messagebox2').hide();
				x=document.getElementById("messagebox");
				$("#messagebox").show();
				x.style.top="30%";
				x.innerHTML=xmlhttp.responseText;
				$("#messagebox").fadeOut(8000);
			}
		}
		xmlhttp.open("POST","../regist_user/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		var postStr = "user_id="+user_id+"&balance="+balance+"&name="+name+"&phone="+phone+"&birth="+birth;
		xmlhttp.send(postStr);
	})
}
function regist_designer_result(xmlhttp){
	$("#regist_designer_tijiao").bind("click",function(){
		designer_ID = $('#regist_designer_ID').val();
		name = $('#regist_designer_name').val();
		phone = $('#regist_designer_phone').val();
		birth = $('#regist_designer_birth').val();
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				y = document.getElementById("regist_designer_box");
				y.style.display ="none";
				$('#messagebox3').hide();
				x=document.getElementById("messagebox");
				$("#messagebox").show();
				x.style.top="30%";
				x.innerHTML=xmlhttp.responseText;
				$("#messagebox").fadeOut(8000);
			}
		}
		xmlhttp.open("POST","../regist_designer/",true);
		xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
		var postStr = "designer_ID="+designer_ID+"&name="+name+"&phone="+phone+"&birth="+birth;
		xmlhttp.send(postStr);
	})
}

$(document).ready(function()
{
	var xmlhttp = createRequest();
	query_button(xmlhttp);
	regist_VIP(xmlhttp);
	regist_Designer(xmlhttp);
	add_money(xmlhttp);
	non_vip(xmlhttp);
	regist_designer_result(xmlhttp);
	regist_VIP_result(xmlhttp);
	vip(xmlhttp);
	$("#regist_user_back").click(
	function()
	{
		$("#messagebox2").hide();
	}
	);

	$("#regist_designer_back").click(
	function()
	{
		$("#messagebox3").hide();
	}
	);



	
});