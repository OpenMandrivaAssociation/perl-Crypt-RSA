%define modname	Crypt-RSA
%define modver	1.99

Summary:	RSA public-key cryptosystem
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Digest-MD2
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Convert-ASCII-Armour
BuildRequires:	perl-Crypt-Primes
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-Tie-EncryptedHash

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the
RSA public-key cryptosystem. It uses Math::Pari(3), a perl
interface to the blazingly fast PARI library, for big
integer arithmetic and number theoretic computations.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

