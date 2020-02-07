@echo off
rem 启用"延缓环境变量扩充"
setlocal EnableDelayedExpansion
set a=1
rem 循环当前目录下所有图片的文件名，支持带空格的名称
for /f "delims=" %%i in ('dir /b *.jpg') do (
rem 如果没有相同的文件名，则继续
if not "%%~ni"=="%~n0" (
if !a! LSS 10 (ren "%%i" "images!a!.jpg") else ren "%%i" "images!a!.jpg"
rem 设置数值型变量a=a+1
set /a a+=1
)
)
echo 批量重命名完成！
pause
