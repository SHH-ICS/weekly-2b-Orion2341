<?php
$radius = floatval(readline("Enter Radius"));
$circumference = 2*pi()*$radius;
$area = pi()*pow($radius, 2);
echo "Circumference =" . $circumference . "\n";
echo "Area =" . $area . "\n";
?>