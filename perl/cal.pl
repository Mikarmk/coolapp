use strict;
use warnings;

my $input = <STDIN>;
chomp $input;

if ($input =~ /^(\d+)\s*([+\-*\/])\s*(\d+)$/) {
    my $num1 = $1;
    my $operator = $2;
    my $num2 = $3;
    
    my $result;
    
    if ($operator eq '+') {
        $result = $num1 + $num2;
    } elsif ($operator eq '-') {
        $result = $num1 - $num2;
    } elsif ($operator eq '*') {
        $result = $num1 * $num2;
    } elsif ($operator eq '/') {
        if ($num2 != 0) {
            $result = $num1 / $num2;
        } else {
            print "Ошибка: деление на ноль\n";
            exit;
        }
    } else {
        print "Ошибка: Неправильный оператор\n";
        exit;
    }
    
    print "$result\n";
} else {
    print "Ошибка: Неправильный формат ввода\n";
}
