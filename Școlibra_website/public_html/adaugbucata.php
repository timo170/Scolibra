<?php
    $host='localhost';
    $username='id20929942_root';
    $pass='1234QWERasdf.';
    $dbname='id20929942_biblioteca';
    
    $conn=mysqli_connect($host,$username,$pass,$dbname);
    if(mysqli_connect_error())
        echo "Conexiunea nu a fost stabilita..".mysqli_connect_error();
    else
    {
        //Preia datele trimise din python
        $json=file_get_contents('php://input');
        //Conversia datelor
        $data=json_decode($json,true);
        $id=$data['Id'];
        $nr=$data['Nr'];
        $query="update carte set Nr='$nr' where Id='$id';";

        if(mysqli_query($conn,$query))
            echo "Datele au fost modificate";
        else
            echo "A aparut o eroare".mysqli_error($conn);
        
        //Inchide conexiunea
        mysqli_close($conn);
    }

?>