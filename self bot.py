from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernamestr = '96522657'
passwordstr = '3454598090'
browser = webdriver.Edge()
browser.get(('http://stu.iust.ac.ir/loginpage.roser'))

################################################################################

<script type="text/javascript">
    var _csrf_token_headers =  {'X-CSRF-TOKEN' : '48891d4e-6e36-41ec-8f30-3404c115590c'};
    function addUniqueParam(jForm) {
        jForm.action = jForm.action;
    }

</script>


    
        
               
        
    


<head>
    <!--[if lte IE 6]>
    <meta http-equiv="REFRESH" content="0;url=/note/ie6_error.html">
    <![ENDIF]-->
    
        <title>سامانه مدیریت امور دانشجویی (سماد) &amp;lt;&amp;gt; داده کاوان اندیشه برتر</title>
        <link rel="icon" href="/res?creatorLogoId=3989&dl=false"
              type="image/jpg" sizes="16x16">
    
    <meta name="heading" content="سماد- سامانه مدیریت امور دانشجویی"/>
    <!--<meta name="menu" content="Login"/>-->
    
    
    
        <meta name="menu" content="AnonymousMenu"/>
    
    <link rel="stylesheet" type="text/css" media="all"
          href="/styles/farsi-fuse/theme.css">

    <!-- JavaScripts Required by DWR -->
    <script type="text/javascript">var context_path = "";</script>
    <script type="text/javascript" src="/scripts/dwr/dwr-service.js"></script>
    <script type='text/javascript' src='/scripts/dwr/engine.js'></script>
    <script type='text/javascript' src='/scripts/dwr/util.js'></script>
    <link href='/styles/KeyBoardStyle.css' rel="stylesheet" type="text/css">
    <script src='/scripts/keyboard.js' type="text/javascript"></script>
    <script type="text/javascript">
        function click_loading() {
            document.getElementById("loading").style.display = "block";
        }
        function show_loading(show) {
            if(show) {
                document.getElementById("loading").style.display = "block";
            }else{
                document.getElementById("loading").style.display = "none";
            }
        }
        function refreshCaptcha() {
            document.getElementById("captcha_img").src = "/captcha.jpg?" + makeid();
        }
        function makeid() {
            var text = "";
            var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            for (var i = 0; i < 8; i++)
                text += possible.charAt(Math.floor(Math.random() * possible.length));
            return text;
        }
        function doCaptcha(res) {
            document.forms["loginForm"].submit();
        }
        function displayCreatorSiteWindows() {
            var stNo = DWRUtil.getValue('studentNumberInput');
            window.open('http://www.dadekavan.ir' + stNo, "mywindow", "menubar=1,resizable=1,width=2048,height=750");
        }
        function displayOrganSiteWindows() {
            var stNo = DWRUtil.getValue('studentNumberInput');
            window.open('http://www.iust.ac.ir' + stNo, "mywindow", "menubar=1,resizable=1,width=2048,height=750");
        }

        function load_cas_server_login_page(){
            window.location.href = '?service=';
        }
    </script>
</head>





<script type="text/javascript" src="/struts/js/base/jquery-1.11.0.min.js"></script>
        <script type="text/javascript" src="/struts/js/base/jquery-ui.min.js?s2j=3.7.1"></script>
            <script type="text/javascript"
                    src="/struts/i18n/jquery.ui.datepicker-fa.min.js?s2j=3.7.1"></script>
<script type="text/javascript" src="/struts/js/plugins/jquery.form.min.js?s2j=3.7.1"></script>
<script type="text/javascript" src="/struts/js/plugins/jquery.subscribe.min.js?s2j=3.7.1"></script>

<script type="text/javascript" src="/struts/js/struts2/jquery.struts2.min.js?s2j=3.7.1"></script>

<script type="text/javascript">
    $(function () {
        jQuery.struts2_jquery.version = "3.7.1";
        jQuery.struts2_jquery.loadAtOnce = true;
        jQuery.scriptPath = "/struts/";
        jQuery.struts2_jquery.local = "fa";
        jQuery.struts2_jquery.gridLocal = "fa";
        jQuery.struts2_jquery.timeLocal = "en";
        jQuery.ajaxSettings.traditional = true;

        jQuery.ajaxSetup({
            cache: false
        });

        jQuery.struts2_jquery.require("js/struts2/jquery.ui.struts2.min.js?s2j=3.7.1");

    });
</script>

    <link id="jquery_theme_link" rel="stylesheet"
          href="/struts/themes/smoothness/jquery-ui.css?s2j=3.7.1" type="text/css"/>

<body id="login">
<div align="center" style="width: 600px;">
</div>
<div id="loading" class="loading_div">
    <img alt="Loading ..." class="loading_icon" align="absmiddle" src="/images/ajax-loader-big.gif"/>
</div>
<div style="top:0px; left:0px; right:0px; bottom:0; background:#FFFFFF; margin:0; position: absolute;">
<div align="center">
<div align="center" style="top:10%;">
    <div>
        <div id="viewHelpDialog"
>
            <div align="center">
                <br>
                <br>
                <br>
                <br>
                <img src="/images/ajax-loader.gif"/>
            </div>
        </div>
<script type='text/javascript'>
jQuery(document).ready(function () { 
	var options_viewHelpDialog = {};
	options_viewHelpDialog.height = 300;
	options_viewHelpDialog.width = 400;
	options_viewHelpDialog.title = "\u0628\u0627\u0632\u06CC\u0627\u0628\u06CC \u06A9\u0644\u0645\u0647 \u0639\u0628\u0648\u0631";
	options_viewHelpDialog.show = "slide";
	options_viewHelpDialog.hide = "slide";
	options_viewHelpDialog.autoOpen = false;
	options_viewHelpDialog.modal = true;
	options_viewHelpDialog.opentopics = "openRemoteDialog1s";
	options_viewHelpDialog.jqueryaction = "dialog";
	options_viewHelpDialog.id = "viewHelpDialog";
	options_viewHelpDialog.href = "#";

jQuery.struts2_jquery_ui.bind(jQuery('#viewHelpDialog'),options_viewHelpDialog);

 });  
</script>

    </div>    <table align="center"
           style="background:url(/images/bg_login.png) no-repeat top center; width:424px; height:290px; margin-top:4%;"
           border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td height="40" valign="top">&nbsp;</td>
        </tr>
        <tr>
            <td valign="top">
                <table width="auto" align="center" border="0"
                       style="margin-top:15px; margin-right:15px; text-align:right; background:none;"
                       cellspacing="0" cellpadding="0">
                    <tr>
                        <td align="left" valign="top">
                            <form action="/j_security_check" method="post" name="loginForm"
                                  id="loginForm">
                                <input type="hidden" name="_csrf"
                                       value="48891d4e-6e36-41ec-8f30-3404c115590c" />
                                <table width="auto" align="center" border="0" style="margin:5px; text-align:right; background:none;"
                                       cellspacing="0" cellpadding="0">
                                    <tr>
                                        <td align="left" valign="top" style="width: 245px; ">
                                            
                                    <table style="text-align:right;" width="245" border="0" cellspacing="0"
                                           cellpadding="0">
                                        <tr>
                                            <td colspan="2" style="height: 15px;"></td>
                                        </tr>
                                        <tr>
                                            <td width="70">
                                                <label for="j_username" class="required desc"
                                                       style=" font:normal 11px tahoma; margin:0px; padding:0px; padding-right:20px;">
                                                    نام کاربری
                                                </label>
                                            </td>
                                            <td height="32"><input type="text" style="width:110px; margin-right: 0px;"
                                                                   name="j_username"
                                                                   id="j_username" tabindex="1"
                                                                   class="keyboardInput"
                                                                   dir="ltr"/>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <label for="j_password" class="required desc"
                                                       style="font:normal 11px tahoma;margin:0px; padding:0px; padding-right:20px;">
                                                    رمز عبور
                                                </label>
                                            </td>
                                            <td height="32"><input type="password" style="width:110px; margin-right: 0px;"
                                                                   name="j_password"
                                                                   id="j_password" tabindex="2"
                                                                   class="keyboardInput" dir="ltr"
                                                AUTOCOMPLETE="off"/>
                                            </td>
                                        </tr>
                                        
                                        <tr>
                                            <td colspan="2" style="padding-right: 25px; padding-bottom: 3px;">
                                                <span style="font-size: 12px;">
                                                عبارت زیر وارد کنید
                                                    </span>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td colspan="2" align="center">
                                                            <img alt="captcha" src="/captcha.jpg" border="0"
                                                                 id="captcha_img">
                                                            <img alt="refresh" src="/images/view-refresh-3.png"
                                                                 border="0" onclick="refreshCaptcha();">
                                                            <input type="text" style="width:40px; margin-right: 0px;"
                                                                   name="captcha_input"
                                                                   id="captcha_input" tabindex="3"
                                                                   class="keyboardInput"
                                                                   dir="ltr"/>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>&nbsp;</td>
                                            <td valign="top">
                                                
                                            </td>
                                        </tr>
                                    </table>
                                            
                                        </td>
                                        <td valign="top" >
                                            <table>
                                                <tr>
                                                    <td>
                                                        <a
                                                                style="padding:0px 0px 2px 2px; margin:0 4px ; line-height:26px; float:left;"
                                                                onclick="displayOrganSiteWindows()"
                                                                href="">
                                                            <img style="height:100px; width:110px; margin-top: 10px;"
                                                                 class="ui-icon-home"
                                                                 src='/res?organLogoId=3988&dl=false' alt='/res?organLogoId=logo.jpg&dl=false'
                                                                 height=100%
                                                                 width=75%/>
                                                        </a>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="center">

                                                    </td>
                                                </tr>
                                            </table>
                                        </td>

                                    </tr>
                                    <tr>
                                        <td colspan="2" valign="top" style="padding-right: 70px;">
                                            <table>
                                                <tr>
                                                    <td>
                                                        
                                                        <input type="submit" class="button" onClick="click_loading()"
                                                               style="font:normal 11px tahoma; height:28px; width:70px; font-size:12px; margin-right:0px; cursor: pointer;"
                                                               name="login" value="ورود"
                                                               tabindex="4" id="login_btn_submit"/>
                                                        
                                                    </td>
                                                    <td width="30px;"></td>
                                                    <td>
                                                        
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </form>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>

</table>
</div>

    <div class="login_message" align="center">
        <div align="center" class="main_body">
            <ul>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3126&dl=false" alt="" width="60" height="60" /><strong>قابل توجه دانشجویان گرامی</strong> 
<strong>خرید غذا به صورت روزفروش به تعداد محدود در ساعتهای 9:30 و 13:00 امکان پذیر می باشد.</strong>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3126&dl=false" alt="" width="60" height="60" /><p><strong>*****قابل توجه دانشجویان گرامی**** مهم<br /></strong></p> 
<p><strong>جهت دریافت اطلاعیه های تغذیه و موارد مهم فوری به کانال تغذیه به آدرس ذیل مراجعه نمائید</strong></p> 
<p><strong><a href="https://telegram.me/TAGHZIYEIUSt" rel="nofollow">https://telegram.me/TAGHZIYEIUSt &nbsp; </a></strong></p> 
<p>&nbsp;</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3128&dl=false" alt="" width="60" height="60" /><p>توجه توجه</p> 
<p>دانشجویانی که تاکنون موفق به ثبت نام وام شهریه نیمسال دوم 97-96 نشده اند تا تاریخ 97/2/9 می توانند با مراجعه به پرتال صندوق رفاه دانشجویان و ارائه مدارک به امور وامهای اداره رفاه نسبت به ثبت نام خود اقدام نمایند.</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3128&dl=false" alt="" width="60" height="60" /><p><strong>دانشجویان گرامی در صورتیکه بعضی از سایت ها از قبیل مهمانسرا، میان وعده و ... را در خارج از دانشگاه نمی توانید مشاهده فرمایید بایستی از vpn&nbsp; استفاده نمایید . برنامه های مربوطه&nbsp; در سایت https://its.iust.ac.ir/service/vpn می باشد .</strong></p> 
<p><strong>مزایای استفاده از VPN‌در دانشگاه</strong></p> 
<ol> 
 <li>VPN این امکان را به وجود می آورد که تمامی ارتباط شما تا دانشگاه رمز شود بنابراین حتی اگر از پروتکلهای نا امن مانند FTP استفاده نمایید می توانید به امنیت اطلاعات خود در طول مسیر اطمینان بیشتری داشته باشید.</li> 
 <li>در صورتیکه بخواهید از امکانات اینترانتی که فقط از داخل دانشگاه&nbsp; قابل دسترسی هستند استفاده نمایید می توانید از VPN‌استفاده نمایید. برای مثال بانکهای اطلاعاتی کتابخانه دانشگاه&nbsp; صرفا از داخل دانشگاه قابل دسترسی است.&nbsp; با استفاده از این سرویس&nbsp; می توانید به این بانکها دسترسی داشته باشید حتی اگر از خارج دانشگاه&nbsp; متصل شده باشید.</li> 
</ol> 
<p><strong>چگونه از این سرویس استفاده نماییم؟</strong></p> 
<p>&nbsp; شما می توانید با نام کاربری و کلمه عبور پرتال خود به سرور VPN دانشگاه وصل شوید. جهت اتصال به VPN دانشگاه، <a href="http://its.iust.ac.ir/sites/default/files/docAttachment/IUST%20VPN%20Connection.pbk" rel="nofollow"><strong>فایل پیوست</strong></a> را دانلود نموده و سپس آنرا اجرا نمایید. حال در پنجره باز شده، نام کاربری و پسورد خود را وارد کرده و در انتها بر روی دکمه Connect کلیک نمایید. برای قطع ارتباط دوباره همان فایل را اجرا کرده و بر روی دکمه Hangup کلیک کنید.</p> 
<p>&nbsp;</p> 
<p><strong>نکات استفاده از سرویس VPN دانشگاه:</strong></p> 
<ol> 
 <li><em>قبل از استفاده از VPN‌ حتما باید ارتباط اینترنت شما برقرار باشد. VPN یک ارتباط مجازی بر روی ارتباط اینترنت شما به وجود می آورد.</em></li> 
 <li><em>اتصال به VPN از داخل دانشگاه و یا اینترانت&nbsp; امکان پذیر نیست و تنها از اینترنت می توانید به این سرویس وصل شوید.</em></li> 
 <li><em>&nbsp;به دلیل اینکه اکثر مشکلات پیش آمده برای اتصال به سرویس VPN (فیلترینگ، شبکه ISP ها، تنظیمات ویندوز کاربران و ..) نامرتبط با دانشگاه می باشد و به دلیل عدم وجود پرسنل برای پاسخگویی به تعداد زیاد کاربران این سرویس، از پاسخگویی به مشکلات عدم اتصال شما معذوریم. این سرویس دائما از نظر سالم بودن چک می شود. لذا در صورت عدم اتصال به VPN یک بار دیگر راهنمایی های موجود در سایت را به دقت مطالعه فرمایید.</em></li> 
 <li><em>&nbsp;سرویس دریافت مقالات، مربوط به کتابخانه مرکزی می باشد. لذا در صورت وجود اشکال یا سوال در این مورد با کتابخانه مرکزی تماس حاصل فرمایید.</em></li> 
</ol> 
<p>Attach File:&nbsp; <a href="https://its.iust.ac.ir/sites/default/files/docAttachment/IUST%20VPN%20Connection.pbk" rel="nofollow">IUST VPN Connection.pbk</a></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <p>دانشجویان برای استفاده خدمان درمانی دانشگاه می باید قبلا با مراجعه به سایت its.iust.ac.ir&nbsp; از مرکز&nbsp; کامپیوتر اکانت گرفته باشند.</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3128&dl=false" alt="" width="60" height="60" /><p>به اطلاع دانشجویان محترم می رساند(استثنائا این هفته به دلیل تعطیلی اول هفته)روز یکشنبه مورخ 97/01/26 سایت نوبت دهی به آدرس ذیل از ساعت 13 الی 14 آماده بازگشایی می باشد دانشجویان محترم با مراجعه به سایت می توانند با گرفتن نوبت از خدمات دندانپزشکی و چشم پزشکی استفاده نمایند</p> 
<p><strong>darman.iust.ac.ir</strong></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <p>قابل توجه اعضاء هیئت علمی کارکنان و دانشجویان دانشگاه</p> 
<p>&nbsp;</p> 
<p><strong>به استحضار می رساند پیرو پیگیری معاونت دانشجوئی دانشگاه از تاریخ 1/12/96 اورژانس 115 دانشگاه با تجهیزات کامل با دو دستگاه آمبولانس و یک دستگاه موتورلانس در ضلع جنوب شرقی دانشگاه جهت ارائه خدمات به جامعۀ دانشگاهی و همچنین مردم منطقه مستقر گردیده است و در صورت وجود شرایط اضطرار تماس با شماره های داخلی 115 و مستقیم </strong><strong>77240568 و </strong><strong>ارائه آدرس مناسب در اسرع وقت در محل حاضر خواهند بود.</strong></p> 
<p><strong>امید است در ادامه نیز بتوان شرایط و امکانات مناسب تری در اختیار دانشگاهیان عزیز قرار داد.</strong></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=13823&dl=false" alt="" width="60" height="60" /><p>سامانه رزرو مهمانسرای دانشجویی دانشگاه علم و صنعت راه اندازی گردید&nbsp; <a rel="nofollow">http://mehmansara.iust.ac.ir</a></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3128&dl=false" alt="" width="60" height="60" /><p><strong>&nbsp;آخرین اخبار معاونت دانشجویی و سایر بخشهای دانشگاه&nbsp; <a href="http://telegram.me/staiust" rel="nofollow">http://telegram.me/staiust </a></strong></p> 
<p>&nbsp;</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=13823&dl=false" alt="" width="60" height="60" /><p><strong>جهت مشاهده اطلاعیه های مربوط به ثبت نام مکانیزه خوابگاه&nbsp;</strong></p> 
<p><strong>دانشجویان کارشناسی ارشد روزانه ورودی 95</strong></p> 
<p><strong>و کارشناسی 95-94-93</strong></p> 
<p><strong>به سایت<a href="http://www.iust.ac.ir/index.php?site=khabgah" rel="nofollow"> khabgah.iust.ac.ir</a> ویا</strong></p> 
<p><strong> کانال تلگرامی <a href="https://t.me/khabgah_iust" rel="nofollow">khabgah@</a> مراجعه فرمایید&nbsp;</strong></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3126&dl=false" alt="" width="60" height="60" /><p><strong>کافی شاپ خوابگاه خواهران در روز های پنج شنبه و جمعه هر هفته غذا سرو می نماید</strong></p> 
<p><strong>&nbsp; <a href="https://telegram.me/gandom_cafe" rel="nofollow">https://telegram.me/gandom_cafe</a>.مشاهده برنامه غذایی در کانال تلگرام</strong></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <p>برنامه کافی شاپ خوابگاه خواهران<br /> 5شنبه ، 5/8/95&nbsp; ناهار(ساعت12 الی13) عدسی، سوپ شیر<br /> جمعه ، 6/8/95 ناهار(ساعت12 الی 13) اسنک، آش رشته<br /> دانشجویان ساکن خوابگاه خواهران از ساعت 12 الی 13 به کافی شاپ خوابگاه خواهران مراجعه کنند.</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <p>دانشجویانی که فاقد بیمه هستند می توانند بدون پرداخت هزینه ای (فقط 1000 تومان بابت صدور دفترچه) دفترچه بیمه سلامت را دریافت نمایند.</p> 
<p>لذا مقتضی است به آدرس زیر مراجعه فرمایید :</p> 
<p>دفتر بیمه سلامت واقع در فرجام بعد از چهارراه حیدرخانی (خاور) روبروی دبیرستان رودباری پلاک 692 شماره تلفن 77492960 و 77493310</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <p><strong>قابل توجه دانشجویان محترم ساکن&nbsp;</strong><strong>کلیه خوابگاه های دانشجویی</strong></p> 
<p><br /><strong>با توجه به الزام نگهبانی کلیه خوابگاهها به کنترل برچسب خوابگاهی نصب شده بر روی کارتهای دانشجویی نیمسال اول 96-95،خواهشمند است تا مورخ 95/8/4 &nbsp;نسبت به پرداخت هزینه خوابگاه و دریافت برچسب اقدام نمایند، بدیهی است در صورت عدم اقدام لازم تا این تاریخ، دسترسی اینترنت این دانشجویان مسدود خواهد گردید</strong></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <p><strong>قابل توجه کلیه دانشجویان محترم ارشد ورودی 95</strong><br /><strong>ساکن خوابگاه حکیمیه</strong><br /><strong>بدینوسیله به اطلاع می رساند با توجه به تعهد قبلی این عزیزان در خصوص تکمیل تسویه حساب رفاهی مقطع کارشناسی در صندوق رفاه، خواهشمند است تا مورخ 95/8/4 در این خصوص اقدامات لازم رابه عمل آورده و جهت تشکیل پروندۀ جدید رفاهی در وقت اداری به کارشناس اسکان مدیریت امور خوابگاهها مراجعه نمایند، بدیهی است در صورت عدم اقدام لازم تا این تاریخ، دسترسی اینترنت این دانشجویان مسدود خواهد گردید</strong></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <p>قابل توجه دانشجویان کارشناسی ارشد ورودی 93 و دانشجویان کارشناسی ورودی90 و 91 و92 جهت مشاهده اطلاعیه های تابستان به : </p> 
<p><a href="http://khabgah.iust.ac.ir" rel="nofollow">khabgah.iust.ac.ir</a> و یا </p> 
<p><a href="http://telegram.me/khabgah_iust" rel="nofollow">http://telegram.me/khabgah_iust</a></p> 
<p>مراجعه نمایید &nbsp;</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3126&dl=false" alt="" width="60" height="60" /><p><strong>به اطلاع دانشجویان گرامی می رساند</strong></p> 
<p><strong>با توجه به اینکه امکان کنسلی غذای رزرو شده بدون کسر هرگونه هزینه ای تا 72 ساعت قبل وجود دارد ضروریست در صورت عدم حضور جهت دریافت غذا، نسبت به کنسل نمودن وعده مورد نظر اقدام فرمائید.ضمنا لازم به توضیح است پس از این فرصت امکان آزاد سازی غذای رزرو شده از طریق صفحه رزرو میسر می باشد و این اقدام صرفا 20 درصد مبلغ غذا را به عنوان کارمزد توسط سیستم کسر خواهد نمود</strong>.</p> 
<p><strong>اداره تغذیه</strong></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=13823&dl=false" alt="" width="60" height="60" /><p><strong>&nbsp; &nbsp; دانشجویان محترمی که نسبت به تشکیل گروه &nbsp;خوابگاه 96-95 اقدام کرده&shy; اند </strong></p> 
<p><strong>جهت مشاهده اطلاعیه روش انتخاب اتاق به سایت خوابگاه به آدرس</strong></p> 
<p><a href="http://khabgah.iust.ac.ir" rel="nofollow"><strong>&nbsp;khabgah.iust.ac.ir&nbsp;</strong></a></p> 
<p><strong>مراجعه نمایند&nbsp;</strong></p> 
<p><strong>&nbsp;</strong>&nbsp;&nbsp;</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=13823&dl=false" alt="" width="60" height="60" /><p><strong>قابل توجه دانشجویان کارشناسی سال 94-93-92 و کارشناسی ارشد روزانه 94 متقاضی استفاده از خوابگاه سال تحصیلی &nbsp;96-95</strong></p> 
<p><strong>سیستم ثبت درخواست خوابگاه 96-95 در فاصله زمانی 15 لغایت 26 اردیبهشت ماه فعال گردیده است لطفا جهت مشاهده اطلاعیه و راهنمای ثبت نام به سایت&nbsp;<a href="http://khabgah.iust.ac.ir/" rel="nofollow">http://khabgah.iust.ac.ir</a>&nbsp;مراجعه نمایید . ضمنا کانال تلگرامی &nbsp;اداره خوابگاه ها به نشانی <a href="http://telegram.me/khabgah_iust" rel="nofollow">telegram.me/khabgah_iust </a>&nbsp;جهت مشاهده اطلاعیه و اخبار نیز فعال می باشد .</strong></p> 
<p>&nbsp;</p> 
<p><strong>&nbsp;</strong></p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <img style="float: right;" src="/res?id=3128&dl=false" alt="" width="60" height="60" /><p>دانشجویان گرامی برای اخذ نوبت در سیستم نوبت دهی مرکز بهداشت و درمان به آدرس <a href="http://medic.iust.ac.ir" rel="nofollow">medic.iust.ac.ir</a> نکات ذیل را مدنظر قرار دهید 1- حتما از فایرفاکس استفاده فرمایید 2- نوبت دهی راس ساعت 13شروع و راس ساعت 14 خاتمه می یابد . راس ساعت 13:30 کل ظرفیت ها های باقیمانده گروههای مختلف فعال می شود &nbsp; حتما 5 دقیقه قبل از ساعت 13 به سایت نوبت دهی لاگین نموده و حتما با دکمه اف 5 صفحه را رفرش نموده و اقدام به اخذ نوبت فرمایید . مسئول نوبت دهی خانم چگینی در مرکز بهداشت و درمان تلفن 2425 می باشد</p>
                    </li>
                
                    <li style="margin:40px;padding: 10px 40px 10px 5px; list-style: none;" >
                        <table> 
 <tbody> 
  <tr> 
   <td><strong>شماره پیامک 30002351007770&nbsp;</strong> <p>معاونت دانشجویی منتظر دریافت پیشنهادات ، انتقادات ،شکایات و اخبار&nbsp;شما از طریق ارسال پیامک به شماره فوق می باشد </p> </td> 
  </tr> 
 </tbody> 
</table>
                    </li>
            </ul>
        </div>
    </div>
<div id="copyright-dab"
     style="position: fixed; font-size:11px; bottom:2px; left:2px; right:2px; height:28px; color: #44677B; background:url(/images/copy_bar.png) repeat-x #CCCCCC; border:1px solid #DBE1E6; ">

    <a style="padding:0px 0px 2px 2px; margin:0 4px ; line-height:26px; float:right;"
       onclick="displayCreatorSiteWindows()"
       href="">
        <img style="padding:0px 10px 2px 2px; margin:0 4px ; line-height:26px; float:right;" class="ui-icon-home"
             src='/res?creatorLogoId=11583&dl=false' alt='/res?creatorLogoId=dab_logo-good.png&dl=false'
             height='30'
             width='30'/>
        داده کاوان اندیشه برتر
    </a>
    <a style="padding:0px 0px 2px 2px; margin:0 4px ; line-height:26px; float:left;" onclick="displayOrganSiteWindows()"
       href="">
        <img style="padding:0px 10px 2px 2px; margin:0 4px ; line-height:26px; float:left;" class="ui-icon-home"
             src='/res?organLogoId=3988&dl=false' alt='/res?organLogoId=logo.jpg&dl=false'
             height='30'
             width='30'/>
        دانشگاه علم و صنعت ایران
    </a>
</div>
</div>
</div>
</body>
################################################################################

username = browser.find_element_by_id('j_username')
username.send_keys(usernamestr)
password = browser.find_element_by_id('j_password')
password.send_keys(passwordstr)
nextButton = browser.find_element_by_id('next')
nextButton.click()
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'Passwd')))
password.send_keys(passwordStr)
signInButton = browser.find_element_by_id('signIn')
signInButton.click()
