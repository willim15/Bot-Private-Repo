use strict;

use WWW::Mechanize;
use HTTP::Cookies;

my $robut = WWW::Mechanize->new();
# Agenta
$robut->agent('User-Agent=Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5');

$robut->cookie_jar(HTTP::Cookies->new);