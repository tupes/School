#!/usr/bin/php

<?php
function main() {
	$url = get_url();
	$file = get_file($url);
	$parser = get_parser();
	html_start();
	parse_xml($file, $parser);
	xml_parser_free($parser);
	html_end();
}

function get_url() {
	// access from environment variables
	// for now just return canned data
	return "products1.xml";
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

function html_end() {
	echo "</table>";
	echo "</body>";
	echo "</html>";
}

function parse_xml($file, $parser) {
	while ($data = fread($file, 4096)) {
		xml_parse($parser, $data, feof($file)); // need to handle xml errors here
	}
}

function start_element($parser, $name, $attrs) {
	//echo $name;
	if ($name == "CATALOG") echo "";
	elseif ($name == "TITLE") echo "<h1>";
	elseif ($name == "PRODUCT") echo "<tr>";
	else echo "<td>";
}

function end_element($parser, $name) {
	switch ($name) {
		case "CATALOG":
			break;
		case "TITLE":
			echo "</h1>"; 
			echo "<table border=1>";
			break;
		case "PRODUCT":
			echo "</tr>";
			break;
		default:
			echo "</td>";
	}
}

function handle_data($parser, $data) {
	echo $data;
}

main();
?>