use strict;
use warnings;

my $sum = 0;
for (my $i = 2; $i <= 999999; $i++){
	my $d0 = int ($i / 100000);
	my $d1 = int(($i / 10000) % 10);
	my $d2 = int(($i / 1000) % 10);
	my $d3 = int(($i / 100) % 10);
	my $d4 = int(($i / 10) % 10);
	my $d5 = int($i % 10);

	my $result = ($d0**5)+($d1**5)+($d2**5)+($d3**5)+($d4**5)+($d5**5);

	if ($result == $i){
		print "$result\n";
		$sum += $result;
	}
}

print "SUM: $sum\n";
