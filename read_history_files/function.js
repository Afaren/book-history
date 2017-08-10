
<html>
<head>
<title>404 error</title>
<script language="javascript" type="text/javascript">
        var i = 5;
        var intervalid;
        intervalid = setInterval("fun()", 1000);
        function fun() {
            if (i == 0) {
                window.location.href = "/opac_two";
                clearInterval(intervalid);
            }
            document.getElementById("mes").innerHTML = i;
            i--;
        }
</script>
</head>

<body>
	<table align="center">
		<tr>
			<td>
				<div style="text-align:center;COLOR: #000000;FONT-WEIGHT: bold; FONT-SIZE: 20px;">
				出错啦~~~您想访问的页面不存在！
				</div>
				<br/>
				<p>将在 <span id="mes">5</span> 秒钟后<a href='/opac_two'>返回首页</a></p>
			</td>
		</tr>
	</table>
</body>
</html>