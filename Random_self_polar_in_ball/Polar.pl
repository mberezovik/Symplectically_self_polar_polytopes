#!/usr/bin/perl
use application "polytope";

### load matrix from file
open(INPUT, "<Vertices.txt");
my $matrix = new Matrix<Rational>(<INPUT>);
close(INPUT);

### create a polytope from the matrix
my $p = new Polytope<Rational>(POINTS=>$matrix);
my $q = polarize($p);
open(OUTPUT,  ">poly_polar_vert.txt");
my $vertnum1 = scalar(@{$q->VERTICES});
for (my $i = 0; $i < $vertnum1;$i++){
	print OUTPUT $q->VERTICES->[$i]."\n";
}
close(OUTPUT);

open(OUTPUT,  ">real_vert.txt");
my $vertnum2 = scalar(@{$p->VERTICES});
for (my $i = 0; $i < $vertnum2;$i++){
	print OUTPUT $p->VERTICES->[$i]."\n";
}
close(OUTPUT);

open(OUTPUT,  ">vertnum_orig.txt");
print OUTPUT $vertnum2."\n";
close(OUTPUT);

open(OUTPUT,  ">vertnum_polar.txt");
print OUTPUT $vertnum1."\n";
close(OUTPUT);