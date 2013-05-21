%define upstream_name    Crypt-RSA
%define upstream_version 1.99

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	RSA public-key cryptosystem
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Digest-MD2
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Convert-ASCII-Armour
BuildRequires:	perl-Crypt-Primes
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-Tie-EncryptedHash
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the
RSA public-key cryptosystem. It uses Math::Pari(3), a perl
interface to the blazingly fast PARI library, for big
integer arithmetic and number theoretic computations.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.990.0-5mdv2012.0
+ Revision: 765136
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.990.0-3
+ Revision: 676522
- rebuild

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.990.0-2
+ Revision: 654902
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.990.0-1mdv2011.0
+ Revision: 406954
- rebuild using %%perl_convert_version

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.99-1mdv2010.0
+ Revision: 383957
- update to new version 1.99

* Wed Jul 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.98-1mdv2009.0
+ Revision: 233035
- update to new version 1.98

* Tue Jul 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.97-1mdv2009.0
+ Revision: 232714
- update to new version 1.97

* Mon Jul 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.95-1mdv2009.0
+ Revision: 232323
- update to new version 1.95

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - rebuild
    - rebuild

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.58-1mdv2008.1
+ Revision: 121757
- kill (multiple!) definitions of %%buildroot on Pixel's request


* Sun Jan 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.58-1mdv2007.0
+ Revision: 105020
- 1.58

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Crypt-RSA

* Fri Nov 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.57-1mdk
- 1.57

* Sat Jul 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.56-1mdk
- 1.56, spec cleanup

* Thu Feb 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.55-1mdk
- 1.55

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.50-3mdk
- rebuild for new perl

