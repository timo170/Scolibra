<?php
    $host='localhost';
    $username='id20929942_root';
    $pass='1234QWERasdf.';
    $dbname='id20929942_biblioteca';

    $conn=mysqli_connect($host,$username,$pass,$dbname);
    if(mysqli_connect_error())
        echo "Conection not established..".mysqli_connect_error();
    else
    {
        //Preia datele de la fisierul care le-a exportat
        $json= file_get_contents('php://input');

        //Converteste datele in variabila PHP
        $data= json_decode($json,true);
        $id=$data['Id'];
        $autor=$data['Autor'];
        $titlu=$data['Titlu'];
        $editura=$data['Editura'];
        $an=$data['An'];
        $nr=$data['Nr'];
        $query="insert into carte values ('$id','$autor','$titlu','$editura','$an','$nr')";
        if(mysqli_query($conn,$query))
        {
            echo "Data stored in a database successfully."
        }
        else
        {
            echo "ERROR: Hush! Sorry $sql.".mysqli_error($conn);
        }
        //Close connection
        mysqli_close($conn);
    }

?>

