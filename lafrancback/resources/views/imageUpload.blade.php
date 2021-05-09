<!DOCTYPE html>
<html>
<head>
    <title>LaFrancCoin Image Upload</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jscroll/2.4.1/jquery.jscroll.min.js"></script>
</head>
    
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
              <a href="sakujoooCloud" class="nav-link">LaFranc Cloud</a>
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

<div class="container">
     
    <div class="panel panel-primary">
      <div class="panel-heading"><h2>LaFrancCoin Image Upload</h2></div>
      <div class="panel-body">
     
        @if ($message = Session::get('success'))
        <div class="alert alert-success alert-block">
            <button type="button" class="close" data-dismiss="alert">×</button>
                <strong>{{ $message }}</strong>
        </div>
        <img src="images/{{ Session::get('image') }}">
        @endif
    
        @if (count($errors) > 0)
            <div class="alert alert-danger">
                <strong>Whoops!</strong> There were some problems with your input.
                <ul>
                    @foreach ($errors->all() as $error)
                        <li>{{ $error }}</li>
                    @endforeach
                </ul>
            </div>
        @endif
    
        <form action="{{ route('image.upload.post') }}" method="POST" enctype="multipart/form-data">
            @csrf
            <div class="row">
    
                <div class="col-md-6">
                    <input type="file" name="image" class="form-control">
                </div>
                <div class="form-group">
                    <label>User Address</label>
                    <input type="text" class="form-control" name="name" required>
                </div>
                <div class="col-md-6">
                    <button type="submit" class="btn btn-success">Upload</button>
                </div>
     
            </div>
        </form>
    
      </div>
    </div>
</div>
</body>
  
</html>