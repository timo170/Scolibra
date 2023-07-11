<?php
if($_POST["submit"]=="query") 
{
    $recipient="timotei.lni@gmail.com";
    $subject="Întrebare de la elevi";
    $sender=$_POST["sender"];
    $senderEmail=$_POST["senderEmail"];
    $message=$_POST["message"];
    $mailBody="Name: $sender\nEmail: $senderEmail\n\n$message";
    mail($recipient, $subject, $mailBody, "From: $sender <$senderEmail>");

    $resSub = "Confirmarea primire e-mail";
    $resBody= "Dear ". $sender ."\n\nMulțumim că ne-ați contactat.\nAcest e-mail este menit să vă informeze că am primit e-mailul dumneavoastră. Vom reveni cu un răspuns cât de curând posibil.";
    $note="\n\nNote : Acesta este un e-mail generat automat.Nu trimiteți răspuns.\nFrom: http://scolibra.000webhostapp.com/";
    $resBody=$resBody . $note;
    mail($senderEmail , $resSub , $resBody);   
    header("location: index.php?response="."Mesajul tău a fost trimis cu succes!"); 
}
?>