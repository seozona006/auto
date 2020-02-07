<?php
get_header();
?>
<!DOCTYPE HTML>
<html lang="<?php echo lang;?>">
<head>
    <meta charset="<?php echo charset;?>">
    <meta name="viewport" content="width=device-width, initial-scale=1,maximum-scale=1,user-scalable=no">
		<meta name="apple-mobile-web-app-capable" content="yes">
		<meta name="apple-mobile-web-app-status-bar-style" content="black">
		<title>
		 <?php 
		  $url = $_SERVER['REQUEST_URI']."";
		  if($url=='/'){
			echo webname." - ".subtitle;
		  }else if($url=='/page/*'){
			echo webname." - ".subtitle."- 第".$url."页";
		  }
		  else
		  {
			echo $the_title." - ".host;
		  }
		  ?>
		</title>
		<!--标准mui.css-->
		<link rel="stylesheet" href="//<?php echo host;?>/templates/media/css/mui.min.css">
		<!--App自定义的css-->
		<link rel="stylesheet" type="text/css" href="//<?php echo host;?>/templates/media/css/app.css" />
		<link rel="stylesheet" type="text/css" href="//<?php echo host;?>/templates/media/style.css" />
</head>
<body>
    <header class="mui-bar mui-bar-nav bgwhite removeshadow">
  			<i class="mui-action-back mui-icon mui-icon-left-nav mui-pull-left"></i>
  			<h1 class="mui-title"></h1>
  			<i class="mui-action-back mui-icon mui-icon-more mui-pull-right"></i>
  			<i class="mui-action-back mui-icon mui-icon-search mui-pull-right"></i>
  	</header>
	