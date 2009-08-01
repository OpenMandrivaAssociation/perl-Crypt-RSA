%define upstream_name    Crypt-RSA
%define upstream_version 1.99

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    RSA public-key cryptosystem
License:    Artistic
Group:      Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-Crypt-Blowfish
BuildRequires:  perl-Crypt-CBC
BuildRequires:  perl-Digest-MD2
BuildRequires:  perl-Digest-SHA1
BuildRequires:  perl-Convert-ASCII-Armour
BuildRequires:  perl-Crypt-Primes
BuildRequires:  perl-Sort-Versions
BuildRequires:  perl-Tie-EncryptedHash
BuildArch:      noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the
RSA public-key cryptosystem. It uses Math::Pari(3), a perl
interface to the blazingly fast PARI library, for big
integer arithmetic and number theoretic computations.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
