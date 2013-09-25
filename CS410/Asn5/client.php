#!/usr/bin/php
Content-Type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta title="CMPUT 410 Assignment 5" http-equiv="content-type" content="text/html;charset=utf-8"/>

	<script type="text/javascript">
		function getItems() {
			
		}
	</script>

</head>
<body>

<?php
	require_once "RESTclient.php";
	// check if user has just clicked 'Add Item'
	if (array_key_exists("price", $_GET)) {
		// create and send a POST request
		$rest = new RESTclient();
		$inputs = get_inputs();
		$url = "url_to_server";
		$rest->createRequest($url, "POST", $inputs);
		$rest->sendRequest();
		// get response
		// $output = $rest->getResponse();
	}
?>

	<h1>Fruit Store</h1>
	Welcome to my fruit store! What can I help you with?
	
	<form action="client.php">
		Name: <input type="text" name="name">
		Price: <input type="text" name="price">
		Description: <input type="text" name="desc">
		<input type="submit" value="Add Item">
	</form>

	<input type="button" value="Get Catalogue" onClick="getItems()">

</body>
</html>