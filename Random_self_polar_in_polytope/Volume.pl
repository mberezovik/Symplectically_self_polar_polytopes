#!/usr/bin/perl
use application "polytope";

### load matrix from file
open(INPUT, "<real_vert.txt");
my $matrix = new Matrix<Rational>(<INPUT>);
close(INPUT);

### create a polytope from the matrix
my $p = new Polytope<Rational>(POINTS=>$matrix);
open(OUTPUT,  ">volume.txt");
print OUTPUT $p->VOLUME."\n";
close(OUTPUT);
