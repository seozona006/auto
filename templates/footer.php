
<!--51la and baidu statistics start-->
<script type="text/javascript" src="https://js.users.51.la/20569117.js"></script>
	<script type="text/javascript" src="https://js.users.51.la/20567633.js"></script>

	<script>
		var _hmt = _hmt || [];
		(function() {
		  var hm = document.createElement("script");
		  hm.src = "https://hm.baidu.com/hm.js?0a5603f19b379f2947cfbf37b1d94cfe";
		  var s = document.getElementsByTagName("script")[0];
		  s.parentNode.insertBefore(hm, s);
		})();
	</script>
<!--51la and baidu statistics end-->

	<div class="fo"><span class="copy">&copy; 2020 <a href="//<?php echo host;?>/"><?php echo webname;?></a></span></div>
	<script src="//<?php echo host;?>/templates/media/js/mui.min.js"></script>
	<script>
		mui.init({
			swipeBack:true //启用右滑关闭功能
		});
		mui('.mui-input-group').on('change', 'input', function() {
			var value = this.checked?"true":"false";
			this.previousElementSibling.innerText = "checked："+value;
		});
	</script>
	</body>
	
</html>