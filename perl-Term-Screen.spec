%define upstream_name    Term-Screen
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A simple all-Perl Term::Cap based screen positioning module
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Term::Screen is a very simple screen positioning module that should
work wherever C<Term::Cap> does. It is set up for Unix using stty's but
these dependences are isolated by evals in the C<new> constructor. Thus
you may create a child module implementing Screen with MS-DOS, ioctl,
or other means to get raw and unblocked input. This is not a replacement
for Curses -- it has no memory.  This was written so that it could be
easily changed to fit nasty systems, and to be available first thing.

The input functions getch, key_pressed, echo, and noecho are implemented
so as to work under a fairly standard Unix system. They use 'stty'
to set raw and no echo modes and turn on auto flush. All of these are
'eval'ed so that this class can be inherited for new definitions easily.

Term::Screen was designed to be "required", then used with object syntax
as shown above. One quirk (which the author was used to so he didn't
care) is that for function key translation, no delay is set. So for many
terminals to get an esc character, you have to hit another char after it,
generally another esc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests seems to be interactive only
#%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/Term
%_mandir/man3/*
