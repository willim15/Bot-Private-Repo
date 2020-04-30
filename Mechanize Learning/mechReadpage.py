begin at login pages
$robut->get('https://www.youtube.com/Login');
$robut->success or die "login GET fail";
my $user = 'woooobar';
my $pass = 'piglet';

# find a fill out the login form
my $login = $robut->form_name("logon");
$login->value('USERID' => $user);
$robut->submit();
$robut->success or die "login POST fail";

print "Login done\n";