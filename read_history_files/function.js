
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
				������~~~������ʵ�ҳ�治���ڣ�
				</div>
				<br/>
				<p>���� <span id="mes">5</span> ���Ӻ�<a href='/opac_two'>������ҳ</a></p>
			</td>
		</tr>
	</table>
</body>
</html>