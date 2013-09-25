#!/usr/bin/php
Content-Type: application/json

<?php
$fruits = json_decode(file_get_contents("fruits.txt"), true);

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
	if ($_SERVER['QUERY_STRING'] == '') {
		// request for all items
		echo json_encode($fruits);
	} else {
		// request for a particular item
		parse_str($_SERVER['QUERY_STRING']);
		echo json_encode($fruits[$id]);
	}
} elseif ($_SERVER['REQUEST_METHOD'] == 'POST') {
	// request to add item
	$_POST = json_decode(file_get_contents("php://input"), true);
	$fruit = array(
		"name" => $_POST["name"], 
		"desc" => $_POST["desc"], 
		"price" => $_POST["price"]
	);
	array_push($fruits, $fruit);
	file_put_contents("fruits.txt", json_encode($fruits));
	echo json_encode($fruits);
}

?>