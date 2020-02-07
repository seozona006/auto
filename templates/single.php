<?php
$cache = file_get_contents(ABPATH."cache/".$title);
preg_match("/<h1>(.*)<\/h1>/i",$cache,$tmp);
$ = $tmp[1];
preg_match("/<\/h1>([\s\S]+)$/i",$cache,$tmp);
$the_content = $tmp[1];
$the_date =filemtime(ABPATH."cache/".$title);
if($title=="" || $cache==""){
	header("HTTP/1.1 404 Not Found");
}
require_once(ABPATH."/lib/content.php");
get_header();
?>

	<div class="bread">
		<a href="//<?php echo host;?>/">Home</a> &gt; <?php echo $;?>
	</div>
   <article class="single">
   <header><h1><?php echo $;?></h1></header>
   <footer>
	<span class="pubdate"><time datetime="<?php echo date("Y-m-d H:i:s",$the_date);?>" pubdate="pubdate"><?php echo date("Y-m-d",$the_date);?></time></span>
   </footer>
		<script src="/templates/media/form1.js"></script>
		<div class="entry-content">
		<?php echo showimglist($the_content)?>
		</div>
		<h2 style="font-size:18px;line-height:30px;color:#086ed5;margin:15px 0;background: #eee;text-indent:10px;border-radius:3px;">近期文章</h2>
		<ul>
		<?php
		$list=new CONTENT(keyfile);
		$list_content = $list->get_the_hot(0,10);
		foreach($list_content as $s){
			echo '<li><a href="//'.host.'/'.$s['titlehash'].'">'.$s['title'].'</a></li>';
		}
		?>
		</ul>
		<h2 style="font-size:18px;line-height:30px;color:#086ed5;margin:15px 0;background: #eee;text-indent:10px;border-radius:3px;">热门文章</h2>
		<ul>
		<?php
		$randlist = $list->get_the_hot(rand(100,200),5);
		foreach($randlist as $list){
		echo '<li><a href="//'.host.'/'.$list['titlehash'].'">'.$list['title'].'</a></li>';
		}
		?>
		</ul>
	</article>

<div style="clear:both"></div>
<?php get_footer();?>
