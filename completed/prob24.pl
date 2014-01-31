my @p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
my $k = 8;

for ($i = 0; $i < 1000000; $i++){
	my $temp = $p[$k];
	$p[$k+1] = $temp;
	print $i . "\n";
}
