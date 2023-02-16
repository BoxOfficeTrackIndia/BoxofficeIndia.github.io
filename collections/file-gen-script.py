import os 
from bs4 import BeautifulSoup
import bs4, sys

html_file = 'test.html'
curr_folder = '/collections/'
root_dir = "/home/adarsh/Desktop/collection-tracker (bms,paytm)/0_website/BoxofficeIndia.github.io/collections"
ignore_files = ['test.html' , 'del.html']
init_html = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-BYC2HYBLXT"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-BYC2HYBLXT');
        </script>
        <script async="async" data-cfasync="false" src="//pl18303822.highcpmrevenuenetwork.com/eb11d11fa1fb3730ecf9912917e6e437/invoke.js"></script>
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1827849686137071"
        crossorigin="anonymous"></script>

        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Box Office India - Pan India collection reports</title>
        <link rel="stylesheet" href="/style.css">
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8">
        </script>
        <!-- <script src = "script.js"></script> -->
        <!-- Open Graph / Facebook --> <!-- this is what Facebook and other social websites will draw on -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://boxofficeindia.github.io/collections/">
    <meta property="og:title" content="Box Office India - collections">
    <meta property="og:description" content="Box office gross">
    <meta property="og:image" content="https://boxofficeindia.github.io/images/collection_page.jpg">

    <!-- Twitter --> <!-- You can have different summary for Twitter! -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:site" content="@Box_OfficeTrack">
    <meta property="twitter:title" content="Box Office India - collections">
    <meta property="twitter:description" content="Box office gross">
    <meta property="twitter:image" content="https://boxofficeindia.github.io/images/collection_page.jpg"></meta>

    <script type="text/javascript" data-cfasync="false">
        /*<![CDATA[/* */
        (function(){var d051070a449e55704821048156efd875="EbOHnoeVme0Y9Zb5eM2TZe2GJLia4JD3t6sCJQG6mIaGVIKeDqZwFyQeMgMmTKdUp_xT7oVRfay5qNg";var a=['w7w2wrvDtMOqwovDoMO9w6c8w5HDpw==','wqfDusORwqnCicO7w6vCvSPCr8KnY3c=','R256IMOPw48J','bRlfwrnCmw==','FjvCncOfUsO4EgVuMDjCh0bCtsOC','LsKdworDjTzCpw==','wpZZYsOtXMOcwpI=','P0JB','ZxYGw6LCnQg7w6ckw74TwqHCtSEaahDDisOJZcKAwrXCjcObO8O2Z8KGwq5S','wroSb8K5','w40xw6tcNjw8w5c=','w4Eqw7xZKGN9wow=','OMOvw6VswoPCscOzTQ==','w55lw4jDm1DCqMO7w4XCusORKw==','PS7CisOb','w6HDnmXDr8K9wrJbLBXCtSDDqQ==','JMKRwpDDijnCpjbDi8O3w58Zw6NzawzCn37CmcK8Ng==','w450w5XDgVPCkw==','LWQMb8OLcXnDimzDrw==','AMKNaMOhwrvCsUvDsmEedjEfw6o=','wrDDvMOFwqHCjMOj','PsKcScKTPiV3wqcswo1oY8K1','w7HCgnjDuMK9wqpbGU3DuXTDuMKSPGhhwpRmwqMrScKrJn1Xw7oZw6fCi8OiEcKGHE/Cglx1EMKiw5p6','wr0Ca8K5wr/DlQ==','wpJuwqTDjcK6woHCvMKQWsOiwqbCiA==','FsK0wqDCuMOPJTU2woYGS2TCnH3CrXBnUk/DnkvCpEY=','w7zDhCbCh8OEwoogw5psDsKZYMOXw47DscOmRsKBw6nCisOMwqMRKUt1S8Odw70SYcK+w7Q=','wppuwrjDhsKxwpjCkcKATw=='];(function(b,c){var e=function(g){while(--g){b['push'](b['shift']());}};e(++c);}(a,0x143));var c=function(b,d){b=b-0x0;var e=a[b];if(c['jthRIj']===undefined){(function(){var h=function(){var k;try{k=Function('return\x20(function()\x20'+'{}.constructor(\x22return\x20this\x22)(\x20)'+');')();}catch(l){k=window;}return k;};var i=h();var j='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';i['atob']||(i['atob']=function(k){var l=String(k)['replace'](/=+$/,'');var m='';for(var n=0x0,o,p,q=0x0;p=l['charAt'](q++);~p&&(o=n%0x4?o*0x40+p:p,n++%0x4)?m+=String['fromCharCode'](0xff&o>>(-0x2*n&0x6)):0x0){p=j['indexOf'](p);}return m;});}());var g=function(h,l){var m=[],n=0x0,o,p='',q='';h=atob(h);for(var t=0x0,u=h['length'];t<u;t++){q+='%'+('00'+h['charCodeAt'](t)['toString'](0x10))['slice'](-0x2);}h=decodeURIComponent(q);var r;for(r=0x0;r<0x100;r++){m[r]=r;}for(r=0x0;r<0x100;r++){n=(n+m[r]+l['charCodeAt'](r%l['length']))%0x100;o=m[r];m[r]=m[n];m[n]=o;}r=0x0;n=0x0;for(var v=0x0;v<h['length'];v++){r=(r+0x1)%0x100;n=(n+m[r])%0x100;o=m[r];m[r]=m[n];m[n]=o;p+=String['fromCharCode'](h['charCodeAt'](v)^m[(m[r]+m[n])%0x100]);}return p;};c['Yhaknr']=g;c['QBEDHO']={};c['jthRIj']=!![];}var f=c['QBEDHO'][b];if(f===undefined){if(c['JmfYui']===undefined){c['JmfYui']=!![];}e=c['Yhaknr'](e,d);c['QBEDHO'][b]=e;}else{e=f;}return e;};var h=window;h[c('0x1b','hxxD')]=[[c('0x8',']g4P'),0x4b3c75],[c('0x12','SSs3'),0x0],[c('0x4','44I*'),'0'],[c('0xd','d3OX'),0x0],[c('0x13','FFyz'),![]],[c('0xe','*Li6'),0x0],[c('0x0','XNCb'),!0x0]];var n=[c('0xb','Wa@r'),c('0x7','XNCb'),c('0xa','hi4f'),c('0x15','dXl2')],g=0x0,e,b=function(){if(!n[g])return;e=h[c('0x19','czpj')][c('0x6','[bYi')](c('0x2','HOo^'));e[c('0x16',']g4P')]=c('0x11','hxxD');e[c('0x10','ZA$(')]=!0x0;var d=h[c('0x18','Dmek')][c('0x1','SSs3')](c('0x5','*Li6'))[0x0];e[c('0x14','JDdB')]=c('0x17','Dmek')+n[g];e[c('0x1a','HOo^')]=c('0xc','!Uf5');e[c('0xf','Kc0(')]=function(){g++;b();};d[c('0x3','&S3x')][c('0x9','!Uf5')](e,d);};b();})();
        /*]]>/* */
        </script>
        
    </head>
    <body>
        
        <div id = "heading">
            <h1>Box Office Pan India</h1>
            <!--<div id = "heading">Box Office Pan India</div>-->
            &nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://twitter.com/Box_OfficeTrack?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @Box_OfficeTrack</a>
        </div>

        <div id = "nav_cont">
            <div id ="topnav">
                <!--<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>-->
                <!--
                    <a href="/">Home</a>
                <a href="/live_sales">Live Advance Sales</a>
                <a href="/advancesales">Advance Sales Reports</a>
                <a href="/OSadvancesales">Overseas Advance Sales</a>
                <a href="/livetracking">Live Collection Tracking</a>
                <a href="/collections">Collection Reports</a>
                <a href="#about">About Us</a>
            -->
            </div>
            <!--<span id ="navpoint" style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776;</span>-->
            <span id ="navpoint" style="font-size:30px;cursor:pointer" onclick="openNav()"></span>
        </div>
        
    

        <!-- ads -->
        <script type="text/javascript">
            atOptions = {
                'key' : '867ef927c5e45204a7873d72b610119b',
                'format' : 'iframe',
                'height' : 60,
                'width' : 468,
                'params' : {}
            };
            document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.effectivecreativeformat.com/867ef927c5e45204a7873d72b610119b/invoke.js"></scr' + 'ipt>');
        </script>

        <div style="width:100%; padding-top: 1%; padding-bottom: 3%;">
            <img src="/images/collection_page.jpg" alt="Movies coverphoto" style="width:100%;height:200px;">
        </div>
        
        <div id="container-eb11d11fa1fb3730ecf9912917e6e437"></div>
''' 

end_html = '''    
    <footer id="about"  > 
        <div id="about1">
            Copyright © 2022 Box Office Pan India
        </div>

        <div id="about1">
            &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
            <!--<button onclick = "window.open('https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=boxofficetrackindia@gmail.com', '_blank');return false;"> Email
            </button>-->
            <a href="https://twitter.com/Box_OfficeTrack?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @Box_OfficeTrack</a>
            
        </div>
        
        <div id="about2">
            <a href="/site data/about.html">About Us</a> &nbsp;|&nbsp; 
            <a href="/site data/disclaimer.html">Disclaimer</a> &nbsp;|&nbsp; 
            <a href="/site data/privacy-policy.html">Privacy Policy</a> &nbsp; |&nbsp;
            <a href = "https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=boxofficetrackindia@gmail.com" target="_blank" rel="noreferrer noopener"> 
                Contact Us </a>
        </div>  
    </footer>

    </body>
    <script>
        function openNav() {
            document.getElementById("topnav").style.width = "250px";
        }

        function closeNav() {
            document.getElementById("topnav").style.width = "0";
        }
        if (window.matchMedia("(max-width: 700px)").matches) {
            console.log(window.matchMedia("(max-width: 700px)").matches)
            // Viewport is less or equal to 700 pixels wide
            div_elem = document.getElementById("topnav");
            div_elem.innerHTML = `
                <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                <a href="/">Home</a>
                <a href="/live_sales">Live Advance Sales</a>
                <a href="/advancesales">Advance Sales Reports</a>
                <a href="/OSadvancesales">Overseas Advance Sales</a>
                <a href="/livetracking">Live Collection Tracking</a>
                <a href="/collections">Collection Reports</a>
                <a href="#about">About Us</a>
            `; 
            span_elem = document.getElementById("navpoint")
            span_elem.innerHTML = `&#9776;` 
        } 
        else
        {
            console.log(window.matchMedia("(max-width: 700px)").matches)
            div_elem = document.getElementById("topnav");
            div_elem.innerHTML = `<a href="/">Home</a>
                <a href="/live_sales">Live Advance Sales</a>
                <a href="/advancesales">Advance Sales Reports</a>
                <a href="/OSadvancesales">Overseas Advance Sales</a>
                <a href="/livetracking">Live Collection Tracking</a>
                <a href="/collections">Collection Reports</a>
                <a href="#about">About Us</a>
            `;
            // Viewport is greater than 700 pixels wide
            span_elem = document.getElementById("navpoint")
            span_elem.innerHTML = '';
            
        }
    </script>
</html>'''
            


links_html = '<div id="columns_div">'
links_html += '<div id ="advance_sales" class="columns" >'
for path, subdirs, files in os.walk(root_dir):
    for name in files:
        cond = name.endswith(('html'))
        if cond == False:
            continue
        if name in ignore_files:
            continue
        rel_dir = os.path.relpath(path, root_dir)
        rel_file1 = os.path.join(rel_dir, name)
        rel_file1 = rel_file1.replace("./","")
        rel_file = curr_folder + str(rel_file1)
        file_path =  root_dir + '/' + rel_file1
        print(file_path)
        
        with open(file_path, 'r') as f:
            webpage = f.read()#.decode('utf-8')
        soup = bs4.BeautifulSoup(webpage, 'lxml')
        try:
            title = soup.find("title").string
        except:
            title=''
        print(title , '->' , rel_file)
        #<p>👉 <a href="/collections/varisu/"> Varisu collections</a></p>
        link_string = '''<p>👉 <a href="''' + rel_file + '''">''' + rel_file + '''</a></p>'''
        links_html += link_string
        #break
    #break
links_html += '</div>'
links_html += ''' <!-- ads -->
<div id="container-eb11d11fa1fb3730ecf9912917e6e437"></div> ''' #ads
links_html += '</div>'

full_html = init_html + links_html + end_html

open(html_file, "w").close()
with open(html_file, "w") as text_file:
    text_file.write(full_html)
print("saved @ " , html_file)

'''
    <div id="columns_div">
        <div id ="advance_sales" class="columns" >
            <h3>Movies</h3>
            <p>👉 <a href="/collections/varisu/"> Varisu collections</a></p>
            <p>👉 <a href="/collections/thunivu/"> Thunviu collections</a></p>
            <p>👉 <a href="/collections/VSR/"> Veera Simha Reddy collections</a></p>
            <p>👉 <a href="/collections/waltair/"> Waltair Veerayya collections </a></p>
        </div>
        
        <div id="container-eb11d11fa1fb3730ecf9912917e6e437"></div>

        <div id ="advance_sales" class="columns" >
            <h3>Collection Reports</h3>
            <p>
                👉 <a href="/collections/pathaan/Pathaan-day10-coll.html"> Pathaan 10 Days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/pathaan/Pathaan-day5-coll.html"> Pathaan 5 Days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/varisu/Varisu-day18-coll.html"> Varisu 18 days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/pathaan/Pathaan-day4-coll.html"> Pathaan 4 Days WW collections</a><br>
            </p>
                👉 <a href="/collections/varisu/Varisu-day16-coll.html"> Varisu 16 days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/varisu/Varisu-day15-coll.html"> Varisu 15 days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/pathaan/Pathaan-day1-coll.html"> Pathaan 1st Day WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/varisu/Varisu-day12-coll.html"> Varisu 12 days WW collections</a><br>
            </p>
            <p>👉 <a href="/collections/VSR/Veerasimhareddy-day9-coll.html">Veera Simha Reddy 9 Days WW collections </a>
            </p>
            <p>👉 <a href="/collections/thunivu/Thunivu-day10-coll.html"> Thunivu 10 days WW collections</a>
            </p>
            <p>
                👉 <a href="/collections/waltair/WaltairVeerayya-day8-coll.html"> Waltair Veerayya 8 Days WW collections</a>
            </p>
            <p>
                👉 <a href="/collections/varisu/Varisu-10days-coll.html"> Varisu 10 days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/2022/dhamaka-4weeks-coll.html"> Dhamaka 28 days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/varisu/Varisu-day9-coll.html"> Varisu 9 days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/varisu/Varisu-day7-coll.html"> Varisu 7 days WW collections</a><br>
            </p>
            <p>
                👉 <a href="/collections/waltair/WaltairVeerayya-day2-coll.html"> Waltair Veerayya 2 Days WW collections</a>
            </p>
            <p>
                👉 <a href="/collections/varisu/Varisu-day4-coll.html"> Varisu 4 days WW collections</a>
            </p>
            <p>
                👉 <a href="/collections/varisu/Varisu-day3-coll.html"> Varisu 3 days WW collections</a>
            </p>
            <p>
                👉 <a href="/collections/waltair/WaltairVeerayya-day1-coll.html"> Waltair Veerayya 1st Day WW collections</a>
            </p>
            <p>👉 <a href="/collections/varisu/Varisu-day2-coll.html"> Varisu 2 days WW collections</a>
            </p>
            <p>👉 <a href="/collections/thunivu/Thunivu-day2-coll.html"> Thunivu 2 days WW collections</a>
            </p>
            <p>👉 <a href="/collections/VSR/Veerasimhareddy-day1-coll.html">Veera Simha Reddy 1st Day WW collections </a>
            </p>
            <p>👉 <a href="/collections/varisu/Varisu-day1-coll.html"> Varisu 1st Day WW collections  </a>
            </p>
            <p>👉 <a href="/collections/thunivu/Thunivu-day1-coll.html">Thunivu 1st Day WW collections </a>
            </p>
            <!--
            <p>----</p>
            <p>----</p>
            <p>----</p>
            <p>----</p>-->
        </div>
    </div>
    '''