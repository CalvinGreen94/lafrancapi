<!-- @section('content') -->

<!DOCTYPE html><html>
	<head>
		<title>sakoju Dashboard</title>

		<link href='//fonts.googleapis.com/css?family=Lato:100' rel='stylesheet' type='text/css'>
		<meta charset="utf-8">
		​<meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0">

		<meta name="_token" content="{{csrf_token()}}" />
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.4.0/min/dropzone.min.css">

		<style>
			body {
				background: url(images/bg.png) no-repeat center center fixed;
				-webkit-background-size: cover;
				-moz-background-size: cover;
				-o-background-size: cover;
				background-size: cover;

				margin: 0;
				padding: 0;
				width: auto;
				height: auto;
				color: #696969;
				display: table;
				font-weight: 100;
				font-family: 'Lato';
			}

			.container {
				text-align: center;
				display: table-cell;
				vertical-align: middle;
			}

			.content {
				text-align: center;
				display: inline-block;
			}

			.title {
				font-size: 96px;
				margin-bottom: 40px;
			}

			.quote {
				font-size: 24px;
			}

			label{
				margin-right:20px;
			}

			form{
				background:#f5f5f5;
				padding:20px;
				border-radius:10px;
			}

			/* input[type="submit"]{
				background:#0098cb;
				border:0px;
				border-radius:5px;
				color:#fff;
				padding:10px;
				margin:20px auto;
			} */

		</style>

	</head>
	<style>
	div.a {
					text-align: center;
	}
	</style>
  <body>
  	<div class='a'><!-- 
    <div class="container">
        <div class="row">
            <div class="col-md-12"> -->
							<div class="links">
								
										<br><a href="dashboard" target="_blank"><button type="submit" class="btn btn-primary btn-block btn-large">Return To Main Dashboard</font></a></button><br>
									<br><a href="homepage" target="_blank"><button type="submit" class="btn btn-primary btn-block btn-large">Return To Homepage</font></a></button><br>
									<br><a href="sakujoooCloud" target="_blank"><button type="submit" class="btn btn-primary btn-block btn-large">Return To sakujo Cloud</a></button><br>
										    <br><a href="c-force.glitch.me" target="_blank"><button type="submit" class="btn btn-primary btn-block btn-large"> Return To VR</a></button><br>

                <a href="https://c-chikara.herokuapp.com"><button type="submit" class="btn btn-primary btn-block btn-large">C-chikara dApp</button></a><br> 
              <a href="https://keiyakusho.herokuapp.com"><button type="submit" class="btn btn-primary btn-block btn-large">Keiyakusho dApp</button></a><br> 
										<header><h3><font color="pink"><img src="/images/cloud.jpg" alt="image" style="width:50%" height="300"></header>
									</h2>
				
							<br><br><br><br><br>
							<!-- <img width="564" align="center" class="mcnImage blockDropTarget" id="dijit__Templated_0" style="border-radius: 22%; padding-bottom: 0px; vertical-align: bottom; display: inline !important; max-width: 589px;" alt="" src="https://gallery.mailchimp.com/0aa44a21110094e02b4951147/images/088641df-8a8c-45a3-bcd7-63882272651b.png" widgetid="dijit__Templated_0"> -->

                <h4 class="text-center font-weight-bold">sakujo Image Upload</h4>
								<h3><p> Please A minimum of 4 images based on .jpeg,.jpg,.png,.gif files..</p></<h3>
									<br><h7>video uploads will happens very soon . i guess i should put some sort of emotional emoji right here..<p style="font-size:75px">&#2764;</p>

									<!-- <h3><p> Images Automatically Upload To The sakujo Cloud Database So Just Click A Link To Be Redirected Away From This Page</p></<h3> -->
                <form method="post" action="{{url('store')}}" enctype="multipart/form-data"
                            class="dropzone" id="dropzone">
                @csrf
                </form>
								<h3><p> Images Automatically Upload To The sakujo Cloud Database <br> Click A Link To Be Redirected Away From This Page</p></<h3><br/>
            </div>
						<!-- <h3><p> Images Automatically Upload To The sakujo Cloud Database <br> Click A Link To Be Redirected Away From This Page</p></<h3><br/> -->

        </div>
    </div>
		<br><br><br><br><br>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.4.0/dropzone.js"></script>
 </body>
 <script type="text/javascript">
    Dropzone.options.dropzone =
     {
        maxFilesize: 10,
        renameFile: function(file) {
            var dt = new Date();
            var time = dt.getTime();
           return time+file.name;
        },
        acceptedFiles: ".jpeg,.jpg,.png,.gif,.mov",
        addRemoveLinks: true,
        timeout: 50000,
        removedfile: function(file)
        {
            var name = file.upload.filename;
            $.ajax({
                headers: {
                            'X-CSRF-TOKEN': $('meta[name="_token"]').attr('content')
                        },
                type: 'POST',
                url: '{{ url("delete") }}',
                data: {filename: name},
                success: function (data){
                    console.log("File has been successfully removed!!");
                },
                error: function(e) {
                    console.log(e);
                }});
                var fileRef;
                return (fileRef = file.previewElement) != null ?
                fileRef.parentNode.removeChild(file.previewElement) : void 0;
        },
        success: function(file, response)
        {
            console.log(response);
        },
        error: function(file, response)
        {
           return false;
        }
    };

    </script>

</html>
