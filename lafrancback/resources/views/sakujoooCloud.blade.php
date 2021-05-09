<!-- @section('content') -->

<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes" />
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        {{-- <meta http-equiv="X-UA-Compatible" content="IE=edge"> --}}
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>LaFrancCoin Cloud</title>
        {{-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous"> --}}
        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,600" rel="stylesheet">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jscroll/2.4.1/jquery.jscroll.min.js"></script>
    </head>
        
 
        <!-- Styles -->
        <style>
            html, body {
                /* background: url('images/bg.jpg') no-repeat center center fixed;
                -webkit-background-size: cover;
                -moz-background-size: cover;
                -o-background-size: cover;
                background-size: cover;
                background-color: #cccccc;
                font-family: 'Nunito', sans-serif;
                font-weight: 200;
                height: auto;
                margin: 0; */
            }

            .full-height {
                height: auto;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            .top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }

            .content {
                text-align: center;
            }

            .title {
                font-size: 84px;
            }

            .links > a {
                color: #FFC0CB;
                padding: 0 25px;
                font-size: 13px;
                font-weight: 600;
                letter-spacing: .1rem;
                text-decoration: none;
                text-transform: uppercase;
            }
.m-b-md {
    margin-bottom: 30px;
}
label{
 margin-right:20px;
}

form{
 background:#f5f5f5;
 padding:20px;
 border-radius:10px;
}
img
{
 width:auto;
 box-shadow:0px 0px 20px #FFFFFF;
 -moz-transform: scale(0.7);
 -moz-transition-duration: 0.6s;
 -webkit-transition-duration: 0.6s;
 -webkit-transform: scale(0.7);

 -ms-transform: scale(0.7);
 -ms-transition-duration: 0.6s;
}
img:hover
{
  box-shadow: 20px 20px 20px #dcdcdc;
 -moz-transform: scale(0.8);
 -moz-transition-duration: 0.6s;
 -webkit-transition-duration: 0.6s;
 -webkit-transform: scale(0.8);

 -ms-transform: scale(0.8);
 -ms-transition-duration: 0.6s;

}
</style>
</head>
<style>
div.a {
        text-align: center;
}
</style>
{{-- <div class="container"> --}}

    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light mb-5">
            <div class="container-fluid">
              <a href="/" class="navbar-brand">LaFranc Testnet</a>
              <button
                class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarNav"
                aria-controls="navbarNav"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                  <li class="nav-item">
                    <a href="http://127.0.0.1:3000/home" class="nav-link">Home</a>
                  </li>
               </ul>
                       <ul class="navbar-nav">
                  <li class="nav-item">
                    <a href="http://127.0.0.1:3000/connect_node" class="nav-link">Connect Node</a>
                  </li>
               </ul>
                              <ul class="navbar-nav">
                  <li class="nav-item">
                    <a href="http://127.0.0.1:3000/get_chain" class="nav-link">Get Chain</a>
                  </li>
               </ul>
                                     <ul class="navbar-nav">
                  <li class="nav-item">
                    <a href="http://127.0.0.1:3000/Validity" class="nav-link">Chain Validity</a>
                  </li>
               </ul>
                                            <ul class="navbar-nav">
                  <li class="nav-item">
                    <a href="http://127.0.0.1:3000/replaced_chain" class="nav-link">Chain Replacements</a>
                  </li>
               </ul>
               <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a href="http://127.0.0.1:3000/login" class="nav-link">User Login/Register</a>
                  </li>
               </ul>
               <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                  <a href="image-upload" class="nav-link">Upload</a>
                </li>
             </ul>  
             <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                  <a href="http://127.0.0.1:3000/c-force" class="nav-link">C-force</a>
                </li>
             </ul>  
            </div>
        </nav>
            </div>
        </nav>

<div class ='a'>
    {{-- <button type="button" class="btn btn-outline-danger"><a href="image-upload">Upload</a></button> --}}

 
<!-- <div class='a'> -->
{{-- <img width="564" align="center" class="mcnImage blockDropTarget" id="dijit__Templated_0" style="border-radius: 22%; padding-bottom: 0px; vertical-align: bottom; display: inline !important; max-width: 589px;" alt="" src="https://gallery.mailchimp.com/0aa44a21110094e02b4951147/images/088641df-8a8c-45a3-bcd7-63882272651b.png" widgetid="dijit__Templated_0"> --}}
<!-- </div> -->
  <body>
      <div class="flex-center position-ref full-height">
          @if (Route::has('login'))
              <div class="top-right links">
                  @auth
                      <!-- <a href="{{ url('/home') }}">Home</a> -->
                  @else
                      <!-- <a href="{{ route('login') }}">Login</a> -->

                      @if (Route::has('register'))
                          <!-- <a href="{{ route('register') }}">Register</a> -->
                      @endif
                  @endauth
              </div>
          @endif

          {{-- <div class="content"> --}}
              <div class="title m-b-md">
                  <!-- sakujooo Cloud -->
                  <header><h3><font color="pink"><img src="/images/cloud.jpg" alt="image" style="width:50%" height="300"></header>
              </div>
                   <div class="lister-item mode-detail" style="height:500px;overflow:scroll;overflow-x:scroll;overflow-y:scroll;border:solid color:yellow">
                    {{-- <div class="card" style="width: 18rem;"> --}}

<?php
$folder_path = 'images/'; //image's folder path

$num_files = glob($folder_path . "*.{JPG,jpg,gif,png,bmp}", GLOB_BRACE);

$folder = opendir($folder_path);

if($num_files > 1)
{
 while(false !== ($file = readdir($folder)))
 {
  $file_path = $folder_path.$file;
  $extension = strtolower(pathinfo($file ,PATHINFO_EXTENSION));
  if($extension=='jpg' || $extension =='png' || $extension == 'gif' || $extension == 'bmp')

  {
   ?>

            <a href="<?php echo $file_path; ?>"><img src="<?php echo $file_path; ?>"  height="200" width='200' /></a>

            <?php
  }
 }
}
else
{
 echo "the folder was empty !";
}
closedir($folder);
?>
<br><br>
<br><br>

</div>

</body>
<br><br><br>
<table width="100%" align="left" class="mcnTextContentContainer" style="max-width: 100%;min-width: 100%;border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;" border="0" cellspacing="0" cellpadding="0">
    <tbody><tr>

        <td class="mcnTextContent" valign="top" style="padding-top: 0;padding-right: 18px;padding-bottom: 9px;padding-left: 18px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;word-break: break-word;color: #FFFFFF;font-family: Helvetica;font-size: 12px;line-height: 150%;text-align: center;">

            <em>Copyright © | 2021 | ProjectGamma.AI| , All rights reserved.</em><br>
<br>
<br>
&nbsp;
        </td>
    </tr>
</tbody></table>
</body>
</html>
</html>
