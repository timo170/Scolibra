<?php
    session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="descriere" content="Carti">
    <meta name="autori" content="Onaca Timotei Dorin și Panda George Marian">
    <title>&#350;colibra website</title>
    <!-- Bootstrap -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="css/my.css" rel="stylesheet">
    <style>
        #books {margin-bottom:50px;}
        @media only screen and (width: 767px) { body{margin-top:150px;}}
        #books .row{margin-top:20px;margin-bottom:10px;font-weight:800;}
        @media only screen and (max-width: 767px) { #books .row{margin-top:10px;}}
    </style>

</head>
<body>
    <nav class="navbar navbar-expand-sm fixed-top">
        <div class="container-fluid bg-warning">
            <div class="navbar-header">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="navbar-brand" href="index.php" style="padding: 1px;"><img class="img-responsive" alt="Brand" src="img/logo.jpg"  style="width: 147px;margin: 5px;">
                        </a>
                    </li>
                </ul>
            </div>
        </div><!-- /.container-fluid -->
    </nav>
    <div id="top" >
        <div class="container-fluid" style="width:112%;margin-left:-6%;margin-right:-6%; background: red;overflow:hidden;">
            <div>
                <form class="example" role="search" method="POST" action="Rezultat.php">
                    <input type="text" class="form-control" name="keyword" style="width:65%;margin:20px 0px 20px 10%;" placeholder="Cauta o carte sau un autor">
                    <button type="submit" style="width:15%;margin:20px 0px 20px 0px;border-radius:5px;"><i class="fa fa-search"></i></button>
                </form>
            </div>
        </div>
    </div>
    <?php
        include "dbconnect.php";
        if(isset($_GET['value']))
            {  
               $_SESSION['category']=$_GET['value'];
            }
        $category=$_SESSION['category'];
        if(isset($_POST['sort']))
        {
            if($_POST['sort']=="autor")
                    {   $query = "SELECT * FROM carte WHERE Categorie='$category' ORDER BY Autor";
                        $result = mysqli_query ($con,$query)or die(mysqli_error($con));
                        ?>
                           <script type="text/javascript">
                              document.getElementById('select').Selected=$_POST['sort'];
                           </script>
                        <?php
                    }
            else
            if($_POST['sort']=="titlu")
                    {   $query = "SELECT * FROM carte WHERE Categorie='$category' ORDER BY Titlu";
                        $result = mysqli_query ($con,$query)or die(mysqli_error($con));
                    }
        } 
        else   
        {   
            $query = "SELECT * FROM carte WHERE Categorie='$category'";
            $result = mysqli_query ($con,$query)or die(mysqli_error($con));
        } 
        $i=0;
        echo '<div class="container-fluid" id="boo">
            <div class="row">
              <div class="col-xs-12 text-center" id="heading">
                     <h2 style="color:rgb(228, 55, 25);text-transform:uppercase;margin-bottom:0px;"> '. $category .'</h2>
               </div>
            </div>      
            <div class="container fluid">
                 <div class="row">
                      <div class="col-sm-5 col-sm-offset-6 col-md-6 col-md-offset-7 col-lg-4 col-lg-offset-8">
                           <form action="';echo $_SERVER['PHP_SELF'];echo'" method="post" class="float-end">
                               <label for="sort">Sortare dupa &nbsp: &nbsp</label>
                                <select name="sort" id="select" onchange="form.submit()">
                                    <option value="default" name="default"  selected="selected">Select</option>
                                    <option value="autor" name="price">Autori in ordine alfabetica  </option>
                                    <option value="titlu" name="priceh">Titluri in ordine alfabetica  </option>
                                </select>
                           </form>
                      </div>
                  </div>
            </div>';
    
            if(mysqli_num_rows($result) > 0) 
            {   
                while($row = mysqli_fetch_assoc($result)) 
                {
                    $path="img/carti/" .$row['Id'].".jpg";
                    $description="Descriere.php?ID=".$row["Id"];
                    if($i%4==0)
                        echo '<div class="row">';
                    echo
                    '<div class="col-sm-6 col-md-3 col-lg-3">
                        <a href="'.$description.'">
                            <div class="book-block" style="border :3px solid #DEEAEE;">
                                <img class="book-center img-responsive" src="'.$path.'">
                                <hr>'.$row["Titlu"].'<br>
                            </div>
                        </a>
                    </div> ';
                    $i++;
                    if($i%4==0)
                        echo '</div>';
                }
            }
        echo '</div>';
    ?>
    <footer style="margin-left:-6%;margin-right:-6%;">
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-1 col-md-1 col-lg-1">
                </div>
                <div class="col-sm-7 col-md-5 col-lg-5">
                    <div class="row text-center">
                        <h2>Să luăm legătura!</h2>
                        <hr class="warning">
                        <p>Încă ești confuz? Sună-ne sau trimite-ne un e-mail și te vom contacta cât mai curând posibil!</p>
                    </div>
                    <div class="row">
                        <div class="col-md-6 text-center">
                            <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><style>svg{fill:#e0f005}</style><path d="M164.9 24.6c-7.7-18.6-28-28.5-47.4-23.2l-88 24C12.1 30.2 0 46 0 64C0 311.4 200.6 512 448 512c18 0 33.8-12.1 38.6-29.5l24-88c5.3-19.4-4.6-39.7-23.2-47.4l-96-40c-16.3-6.8-35.2-2.1-46.3 11.6L304.7 368C234.3 334.7 177.3 277.7 144 207.3L193.3 167c13.7-11.2 18.4-30 11.6-46.3l-40-96z"/></svg>
                            <p><a href="tel:0738231065">0738231065</a></p>
                        </div>
                       <div class="col-md-4 text-center">
                            <a href="https://wa.me/40738231065" title="Deschide conversația Whatsapp" target="_blank"> <img src="img/WhatsAppButtonGreenSmall.png"> </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <div class="container">
        <!-- Trigger the modal with a button -->
        <button type="button" id="query_button" class="btn btn-lg" data-bs-toggle="modal" data-bs-target="#query">Trimite email</button>
        <!-- Modal -->
        <div class="modal fade" id="query" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header text-center">
                        <button type="button" class="close" data-bs-dismiss="modal">&times;</button>
                        <h4 class="modal-title">Scrie mesajul aici</h4>
                    </div>
                    <div class="modal-body">           
                        <form method="post" action="query.php" class="form" role="form">
                            <div class="form-group">
                                <label class="sr-only" for="name">Nume</label>
                                <input type="text" class="form-control"  placeholder="Numele tau" name="sender" required>
                            </div>
                            <div class="form-group">
                                <label class="sr-only" for="email">Email</label>
                                <input type="email" class="form-control" placeholder="abc@gmail.com" name="senderEmail" required>
                            </div>
                            <div class="form-group">
                                <label class="sr-only" for="query">Mesaj</label>
                                <textarea class="form-control" rows="5" cols="30" name="message" placeholder="Mesajul tau" required></textarea>
                            </div>
                            <div class="form-group">
                                <button type="submit" name="submit" value="query" class="btn btn-block">
                                    Trimite mesaj
                                </button>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>  
        </div>
    </div>
</body>
</html>