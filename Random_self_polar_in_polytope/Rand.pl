#!/usr/bin/perl
use application "polytope";

### load matrix from file
open(INPUT, "<Default.txt");
my $matrix = new Matrix<Rational>(<INPUT>);
close(INPUT);

# ### create a polytope from the matrix
my $p = new Polytope<Rational>(POINTS=>$matrix);
my $q = unirand($p,4);
open(OUTPUT,  ">not_sym.txt");
my $vertnum = scalar(@{$q->VERTICES});
for (my $i = 0; $i < $vertnum;$i++){
	print OUTPUT $q->VERTICES->[$i]."\n";
}
close(OUTPUT);
