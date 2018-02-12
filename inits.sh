

#!/usr/bin/env bash
# -------------------------------------------------------
# TITLE
# install_chromedriver_mac.sh
# DESCRIPTION
# 用于自动下载指定版本的驱动
# AUTHOR
# bixiaopeng &lt;wirelessqa@163.com&gt;
# DEPENDENCIES
# Operating System: Works on mac OS
# Shell: bash preferred.
# HOWTO
# bash install_chromedriver_mac.sh &lt;版本号&gt;
# bash install_chromedriver_mac.sh # 会下载默认的2.24版本
#
# -------------------------------------------------------
# CHANGELOG
# 16/9/21 上午10:56 bixiaopeng initial version created.

CHROME_DRIVER_VERSION=2.24

version=61 # 输入的版本号

# 判断是否为空
if [[ -z ${version} ]];then echo "- Version param is empty. set default version=${CHROME_DRIVER_VERSION}" &amp;&amp; version=${CHROME_DRIVER_VERSION};fi

echo "- Download version ${version}"

# chrome driver 驱动文件下载固定 URL ,不要攺动哦。
CHROME_DRIVER_BASE_URL="http://chromedriver.storage.googleapis.com/index.html?path=${CHROME_DRIVER_VERSION}/"
CHROME_DRIVER_URL_MAC=${CHROME_DRIVER_BASE_URL}"chromedriver_mac64.zip"

# mac 版的压缩包名
ZIP_FILE_NAME="chromedriver_mac64.zip"
# 解压后的名字
CMD_FILE_NAME="chromedriver"

function download_chromedriver()
{
 echo - Download ${ZIP_FILE_NAME} from ${CHROME_DRIVER_URL_MAC}
 curl -O -X GET -H "X-DevTools-Emulate-Network-Conditions-Client-Id: 31f262af-532f-47ed-89f6-6bae5b7b4e3f" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36" -H "X-Client-Data: CJe2yQEIpLbJAQjBtskBCPKcygE=" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Referer: http://chromedriver.storage.googleapis.com/index.html?path=${CHROME_DRIVER_VERSION}/" -H "Accept-Encoding: gzip, deflate, sdch" -H "Accept-Language: zh-CN,zh;q=0.8,en;q=0.6" -H "Cache-Control: no-cache" -H "Postman-Token: 7abaa68b-1cbe-5629-a8de-5efb85d80fe4" "http://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/${ZIP_FILE_NAME}"

 if [[ ! -f ${ZIP_FILE_NAME} ]]
 then
 echo "&gt;&gt; Fail download."
 exit 0
 else
 echo "&gt;&gt; Success download."
 fi
}

function unzip_file()
{
 unzip ${ZIP_FILE_NAME}
 if [[ -f ${CMD_FILE_NAME} ]];then echo "- Unzip success.";else echo "- Unzip fail." &amp;&amp; exit 0;fi
}

function init_env()
{
 rm ${ZIP_FILE_NAME}
 rm ${CMD_FILE_NAME}
}

echo "第1步: 初始化环境,然后下载${version}版本的压缩文件"
init_env
download_chromedriver

echo "第2步: 解压"
unzip_file

echo "第3步: 把命令文件复制到指定目录"
cp ${CMD_FILE_NAME} /usr/local/bin

echo "第4步: 查看chrome driver 版本"
chromedriver -v
