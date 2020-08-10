<?php

if (isset($_POST['submit'])) {
  $name = $_Post['name'];
  $email = $_Post['email'];
  $mailFrom = $_Post['mail'];
  $message = $_Post['message'];

  $mailTo = "dulles.tsa@gmail.com";
  $headers = "From: ".$mailFrom;
  $txt = "You have received an e-mail from ".$name.".\n\n".$message;

  mail($mailTo, 'Contact Form Submission', $txt, $headers);
  header("Location: contact.html")
}

 ?>
