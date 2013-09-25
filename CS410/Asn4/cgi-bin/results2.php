#!/usr/bin/php
Content-Type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head></head>
<body>

<?php

// GLOBAL VARIABLES
$total = 0;
$price = 0;
$on_price = false;
$on_quantity = false;
$on_image = false;

function main() {
	$url = get_url();
	$file = get_file($url);
	$parser = get_parser();
	//html_start();
	parse_xml($file, $parser);
	xml_parser_free($parser);
	html_end();
}

function get_url() {
	// access from environment variables
	// for now just return canned data
	//return "products1.xml";
	return $_GET['url'];
}

function get_file($url) {
	return fopen($url, "r");
}

function get_parser() {
	$parser = xml_parser_create();
	xml_set_element_handler($parser, "start_element", "end_element");
	xml_set_character_data_handler($parser, "handle_data");
	return $parser;
}

function html_start() {
	echo "<html>";
	echo "<head>";
	echo "</head>";
	echo "<body>";
}

function parse_xml($file, $parser) {
	while ($data = fread($file, 4096)) {
		xml_parse($parser, $data, feof($file)); // need to handle xml errors here
	}
}

function start_element($parser, $name, $attrs) {
	global $on_quantity, $on_price, $on_image;
	switch ($name) {
		case "CATALOG": 
			break;
		case "TITLE": 
			echo "<h1>";
			break;
		case "PRODUCT": 
			echo "<tr>";
			break;
		case "ID":
			echo "<td>";
			break;
		case "NAME":
			echo "<td>";
			break;
		case "SPECS":
			echo "<td>";
			break;
		case "PRICE":
			$on_price = true;
			echo "<td>";
			break;
		case "QUANTITY":
			$on_quantity = true;
			echo "<td>";
			break;
		case "IMAGE":
			$on_image = true;
			echo "<td>";
			break;
		default:
			echo "error";
	}
}

function end_element($parser, $name) {
	global $on_quantity, $on_price, $on_image;
	switch ($name) {
		case "CATALOG":
			break;
		case "TITLE":
			echo "</h1>";
			echo "<table border=1>";
			echo "<tr><th>Product</th><th>Name</th><th>Description</th><th>Price</th><th>Quantity</th><th>Image</th></tr>";
			break;
		case "PRODUCT":
			echo "</tr>";
			break;
		case "ID":
			echo "</td>";
			break;
		case "NAME":
			echo "</td>";
			break;
		case "SPECS":
			echo "</td>";
			break;
		case "PRICE":
			$on_price = false;
			echo "</td>";
			break;
		case "QUANTITY":
			$on_quantity = false;
			echo "</td>";
			break;
		case "IMAGE":
			$on_image = false;
			echo "</td>";
			break;
		default:
			echo "error";
	}
}

function handle_data($parser, $data) {
	global $on_quantity, $on_price, $on_image, $total, $price;
	if ($on_quantity) {
		$total +=  $price * (int)$data;
	}
	elseif ($on_price) {
		$price = (int)$data;
	}
	elseif ($on_image) {
		$data = '<img src="' . $data . '">';
	}
	echo $data;
}

function html_end() {
	global $total;
	echo "</table>";
	echo "Total value of remaining quantities = $" . $total;
}

main();
?>

</body>
</html>