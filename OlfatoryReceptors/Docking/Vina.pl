#!/usr/bin/perl
# print"Ligand_file:\t";
my $argument = $ARGV[0];

# $ligfile=<STDIN>;
# chomp $ligfile;
# print$ligfile;
$ligfile="Ligandos.txt";
open (FH,$ligfile)||die "Cannot open file\n";
@arr_file=<FH>;

for($i=0;$i<@arr_file;$i++)
{
print"@arr_file[$i]\n";
@name=split(/\./,@arr_file[$i]);
}
for($i=0;$i<@arr_file;$i++)
{
	chomp @arr_file[$i];
	print"@arr_file[$i]\n";
	system("vina --config conf.txt --ligand Ligandos/PDBQT/@arr_file[$i] > Dockings/$argument/@arr_file[$i].log");
}