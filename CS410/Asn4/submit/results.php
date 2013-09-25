#!/usr/bin/php
Content-Type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta title="CMPUT 410 Assignment 4" http-equiv="content-type" content="text/html;charset=utf-8"/>
</head>
<body>

<?php

// GLOBAL VARIABLES
$output = "";
$total = 0;
$price = 0;
$on_price = false;
$on_quantity = false;
$on_image = false;
parse_str($_SERVER['QUERY_STRING']);
// for some reason using _GET wasn't working on my computer
//var_dump($_GET);
//$url = $_GET["url"];

function main() {
	global $output, $url;
	$file = fopen($url, "r");
	if (!$file) die("Invalid URL for XML File");
	$parser = get_parser();
	parse_xml($file, $parser);
	xml_parser_free($parser);
	html_end();
	echo $output;
}

function get_parser() {
	$parser = xml_parser_create();
	xml_set_element_handler($parser, "start_element", "end_element");
	xml_set_character_data_handler($parser, "handle_data");
	return $parser;
}

function parse_xml($file, $parser) {
	while ($data = fread($file, 4096)) {
		xml_parse($parser, $data, feof($file)) 
		|| 
		die (sprintf("XML Error: %s at line %d", 
				xml_error_string(xml_get_error_code($parser)),
				xml_get_current_line_number($parser)));
	}
}

function start_element($parser, $name, $attrs) {
	global $output, $on_quantity, $on_price, $on_image, $price;
	switch ($name) {
		case "CATALOG": 
			break;
		case "TITLE": 
			$output .= "<h1>";
			break;
		case "PRODUCT": 
			$output .= "<tr>";
			break;
		case "ID":
			$output .= "<td>";
			break;
		case "NAME":
			$output .= "<td>";
			break;
		case "SPECS":
			$output .= "<td>";
			break;
		case "PRICE":
			$price = 0;
			$on_price = true;
			$output .= "<td>";
			break;
		case "QUANTITY":
			$on_quantity = true;
			$output .= "<td>";
			break;
		case "IMAGE":
			$on_image = true;
			$output .= "<td>";
			break;
		default:
			die("Unknown Element in XML Document");
	}
}

function end_element($parser, $name) {
	global $output, $on_quantity, $on_price, $on_image;
	switch ($name) {
		case "CATALOG":
			break;
		case "TITLE":
			$output .= "</h1>";
			$output .= "<table border=1>";
			$output .= "<tr><th>Product</th><th>Name</th><th>Description</th><th>Price</th><th>Quantity</th><th>Image</th></tr>";
			break;
		case "PRODUCT":
			$output .= "</tr>";
			break;
		case "ID":
			$output .= "</td>";
			break;
		case "NAME":
			$output .= "</td>";
			break;
		case "SPECS":
			$output .= "</td>";
			break;
		case "PRICE":
			$on_price = false;
			$output .= "</td>";
			break;
		case "QUANTITY":
			$on_quantity = false;
			$output .= "</td>";
			break;
		case "IMAGE":
			$on_image = false;
			$output .= "</td>";
			break;
		default:
			die("Unknown Element in XML Document");
	}
}

function handle_data($parser, $data) {
	global $output, $on_quantity, $on_price, $on_image, $total, $price;
	if ($on_quantity) {
		$total +=  $price * (int)$data;
	}
	elseif ($on_price) {
		$price = (int)$data;
		$output .= "$";
	}
	elseif ($on_image) {
		$data = '<img src="' . $data . '">';
	}
	$output .= $data;
}

function html_end() {
	global $output, $total;
	$output .= "</table>";
	$output .= "Total value of remaining quantities = $" . $total;
}

main();
?>

</body>
</html>