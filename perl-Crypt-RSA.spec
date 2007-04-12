%define realname Crypt-RSA

Name:           perl-%{realname}
Version:	    1.58
Release:        %mkrel 1
License:        Artistic
Group:          Development/Perl
Summary:        RSA public-key cryptosystem
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{realname}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{realname}/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  perl-devel
BuildRequires:  perl-Crypt-Blowfish
BuildRequires:  perl-Crypt-CBC
BuildRequires:  perl-Digest-MD2
BuildRequires:  perl-Digest-SHA1
BuildRequires:  perl-Convert-ASCII-Armour
BuildRequires:  perl-Crypt-Primes
BuildRequires:  perl-Sort-Versions
BuildRequires:  perl-Tie-EncryptedHash
Requires:       perl
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the
RSA public-key cryptosystem. It uses Math::Pari(3), a perl
interface to the blazingly fast PARI library, for big
integer arithmetic and number theoretic computations.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/*/*


