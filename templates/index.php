<?php
require_once(ABPATH."/lib/content.php");
$list = new CONTENT(keyfile);
$offset = ($page-1)*10;
$the_content = $list->get_the_list($offset);
get_header();
?>
<div class="mui-content">
			<div id="header">
				<div class="avatar mui-text-center">
					<img src="/templates/media/fonts/60x60.gif" alt=""/>
				</div>
				<div class="per-info">
					<div class="title-name"><?php echo webname; ?></div>
					<div class="present mui-ellipsis-2">http://<?php echo host;?>/<i class="mui-icon mui-icon-arrowdown"></i></div>
					<div class="post-info">791篇原创内容</div>
				</div>
				<div class="follow-us mui-text-center"><a href="http://www.yb5175.top" rel="nofollow">关注公众号</a></div>
			</div>
			<?php
				foreach($the_content as $single){
				?>
			<div class="time mui-text-center"><?php echo date("Y-m-d H:i:s",$single['mdate']);?></div>
			<div class="mui-card card-list" id="post-<?php echo $single['id']?>">
				<ul class="mui-table-view">
					<a href="//<?php echo host;?>/<?php echo $single['titlehash']?>">
						<div class="mui-card-header mui-card-media post-title" style="position:relative;height:40vw;background:linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url(./templates/media/images/images<?php echo rand(1,1753);?>.jpg) no-repeat;background-position:center top;    background-size: 100% AUTO;">
							<p class="mui-ellipsis-2"><?php echo $single['title'];?></p>
						</div>
					</a>
					<li class="mui-table-view-cell mui-media">
				        <a href="//<?php echo host;?>/<?php echo $single['titlehash']?>">
				            <img class="mui-media-object mui-pull-right" src="./templates/media/banner<?php echo rand(1,18);?>.jpg">
				            <div class="mui-media-body">
				                <div class="post-title-list mui-ellipsis-2"><?php echo getabstract($single['content'], 45);?>...</div>
				            </div>
				        </a>
				    </li>
				</ul>
			</div>
			<?php
				}
			echo $list->pageinfo();
			?>

		</div>
		
		<?php get_footer();?>

