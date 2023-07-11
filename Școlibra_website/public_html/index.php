<?php
    session_start();
    include "dbconnect.php";
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
    <link href="css/my.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .autor-block {margin-top:20px;padding:5px;background:#fff; border :1px solid #DEEAEE;border-radius:10px;}
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-sm fixed-top">
        <div class="container-fluid bg-warning">
            <div class="navbar-header">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="navbar-brand" href="#" style="padding: 1px;"><img class="img-responsive" alt="Brand" src="img/logo.jpg"  style="width: 147px;margin: 5px;">
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
        <div class="container-fluid" id="header">
            <div class="row">
                <div class="col-md-4 col-lg-4" >
                    <div style="background:#D67B22;color:#fff;font-weight:800;border:none;padding:15px;"> Categorii
                    </div>
                    <ul id="category">
                        <li> <a href="Produs.php?value=Beletristică"> Beletristică </a> </li>
                        <li> <a href="Produs.php?value=Memorii,biografii,jurnale"> Memorii,biografii,jurnale </a> </li>
                        <li> <a href="Produs.php?value=Manuale%20și%20auxiliare%20școlare"> Manuale și auxiliare școlare </a> </li>
                        <li> <a href="Produs.php?value=Sociologie"> Sociologie </a> </li>
                        <li> <a href="Produs.php?value=Filozofie"> Filozofie </a> </li>
                        <li> <a href="Produs.php?value=Practice%20și%20timp%20liber"> Practice și timp liber </a> </li>
                        <li> <a href="Produs.php?value=Business%20and%20Management"> Business & Management </a> </li>
                        <li> <a href="Produs.php?value=Health%20and%20Cooking"> Health and Cooking </a> </li>
                    </ul>
                </div>
                <div class="col-md-8 col-lg-8">
                    <!-- Carousel -->
                    <div id="myCarousel" class="carousel slide" data-bs-ride="carousel">
                        <!-- Indicators/dots -->
                        <div class="carousel-indicators">
                            <button type="button" data-bs-target="myCarousel" data-bs-slide-to="0" class="active"></button>
                            <button type="button" data-bs-target="myCarousel" data-bs-slide-to="1"></button>
                            <button type="button" data-bs-target="myCarousel" data-bs-slide-to="2"></button>
                            <button type="button" data-bs-target="myCarousel" data-bs-slide-to="3"></button>
                            <button type="button" data-bs-target="myCarousel" data-bs-slide-to="4"></button>
                            <button type="button" data-bs-target="myCarousel" data-bs-slide-to="5"></button>
                        </div>
                        <!-- The slideshow/carousel -->
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img src="img/carusel/1.jpg" class="d-block w-100 img-responsive">
                            </div>
                            <div class="carousel-item">
                                <img src="img/carusel/2.jpg" class="d-block w-100 img-responsive">
                            </div>
                            <div class="carousel-item">
                                <img src="img/carusel/3.jpg" class="d-block w-100 img-responsive">
                            </div>
                            <div class="carousel-item">
                                <img src="img/carusel/4.jpg" class="d-block w-100 img-responsive">
                            </div>
                            <div class="carousel-item">
                                <img src="img/carusel/5.jpg" class="d-block w-100 img-responsive">
                            </div>
                            <div class="carousel-item">
                                <img src="img/carousel/6.jpg" class="d-block w-100 img-responsive">
                            </div>
                        </div>
                        <!-- Left and right controls/icons -->
                        <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon"></span>
                        </button>
                        <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
                            <span class="carousel-control-next-icon"></span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <?php
        $query = "SELECT Id,Titlu FROM carte ORDER BY Id DESC LIMIT 4";
        $result = mysqli_query ($con,$query)or die(mysqli_error($con));
        if(mysqli_num_rows($result) > 0) 
            {   
                $i=0;
                echo '<div class="container-fluid text-center" id="new">';
                    echo '<div class="row">';
                    while($i<4) 
                    {
                        $row = mysqli_fetch_assoc($result);
                        $path="img/carti/" .$row['Id'].".jpg";
                        $description="Descriere.php?ID=".$row["Id"];
                        echo 
                        '<div class="col-sm-6 col-md-3 col-lg-3">
                            <a href="'.$description.'">
                                <div class="book-block" style="border :3px solid #DEEAEE;">
                                    <div class="tag">Nou</div>
                                    <div class="tag-side"><img src="img/tag.png"></div>
                                    <img class="book-center img-responsive" src="'.$path.'">
                                    <hr>'.$row["Titlu"].'<br>
                                </div>
                            </a>
                        </div> ';
                        $i++;
                    }
                    echo '</div>
                </div>';
            }
        else {
            echo '<div>Eroare</div>';
        }
    ?>
    
    <div class="container-fluid" id="author">
        <h3 style="color:#D67B22;"> SCRIITORI IMPORTANȚI </h3>
        <div class="row">
            <div class="col-sm-6 col-md-3 col-lg-3">
                <a href="autori/mihai_eminescu.html">
                    <div class="autor-block">
                        <img class="book-center img-responsive" src="img/autori/mihai_eminescu.jpg">
                    </div>
                </a> 
            </div>
            <div class="col-sm-6 col-md-3 col-lg-3">
                <a href="autori/marin_preda.html">
                    <div class="autor-block">
                        <img class="book-center img-responsive" src="img/autori/marin_preda.jpg">
                    </div>
                </a>
            </div>
            <div class="col-sm-6 col-md-3 col-lg-3">
                <a href="autori/ioan_slavici.html">
                    <div class="autor-block">
                        <img class="book-center img-responsive" src="img/autori/ioan_slavici.jpg">
                    </div>
                </a>
            </div>
            <div class="col-sm-6 col-md-3 col-lg-3">
                <a href="autori/ion_creanga.html">
                    <div class="autor-block">
                        <img class="book-center img-responsive" src="img/autori/ion_creanga.jpg">
                    </div>
                </a>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-6 col-md-3 col-lg-3">
                <a href="autori/costache_negruzzi.html">
                    <div class="autor-block">
                        <img class="book-center img-responsive" src="img/autori/costache_negruzzi.jpg">
                    </div>
                </a>
            </div>
            <div class="col-sm-6 col-md-3 col-lg-3">
                <a href="autori/george_bacovia.html">
                    <div class="autor-block">
                        <img class="book-center img-responsive" src="img/autori/george_bacovia.jpg">
                    </div>
                </a>
            </div>
            <div class="col-sm-6 col-md-3 col-lg-3">
                <a href="autori/vasile_alecsandri.html">
                    <div class="autor-block">
                        <img class="book-center img-responsive" src="img/autori/vasile_alecsandri.jpg">
                    </div>
                </a>
            </div>
            <div class="col-sm-6 col-md-3 col-lg-3">
                <a href="autori/george_cosbuc.html">
                    <div class="autor-block">
                        <img class="book-center img-responsive" src="img/autori/george_cosbuc.jpg">
                    </div>
                </a>
            </div>
        </div>
    </div>
    <footer style="margin-left:-6%;margin-right:-6%;">
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-1 col-md-1 col-lg-1">
                </div>
                <div class="col-sm-7 col-md-5 col-lg-5">
                    
                    <div class="row">
                        <div class="col-md-4 text-center">
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