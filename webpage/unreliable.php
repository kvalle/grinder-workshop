<? 
$random = rand(0,100);
if($random < 1) {
	header("HTTP/1.1 503 Service Unavailable");
} else {
	print(Date("Y.m.d H:s")); 
}
?>