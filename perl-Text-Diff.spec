%{?scl:%scl_package perl-Text-Diff}

Name:           %{?scl_prefix}perl-Text-Diff
Version:        1.44
Release:        3%{?dist}
Summary:        Perform diffs on files and record sets
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic) and MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Diff/
Source0:        http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/Text-Diff-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Algorithm::Diff) >= 1.19
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional run-time:
BuildRequires:  %{?scl_prefix}perl(utf8)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(Test)
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Algorithm::Diff) >= 1.19

# Remove under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(Algorithm::Diff)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Algorithm::Diff\\)$
%endif

%description
Text::Diff provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is better
integrated with Perl and available on all platforms. It is often faster
than shelling out to a system's diff executable for small files, and
generally slower on larger files.

%prep
%setup -q -n Text-Diff-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 1.44-3
- SCL

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-2
- Perl 5.24 rebuild

* Sat Feb 27 2016 Petr Šabata <contyk@redhat.com> - 1.44-1
- 1.44 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Petr Šabata <contyk@redhat.com> - 1.43-1
- 1.43 bump
- Updated source URL
- Modernized the spec file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-11
- Perl 5.22 rebuild

* Thu Jan 15 2015 Petr Pisar <ppisar@redhat.com> - 1.41-10
- Specify all dependencies

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.41-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-4
- Update license

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.41-2
- Perl 5.16 rebuild

* Fri Jan 27 2012 Petr Šabata <contyk@redhat.com> - 1.41-1
- 1.41 bump, spec modernization and cleanup
- Update Source URL

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.37-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.37-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.37-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.37-3
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.37-2
- add Test::More as a BR (rt#50040)

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.37-1
- add filtering
- auto-update to 1.37 (by cpan-spec-update 0.01)
- altered br on perl(Algorithm::Diff) (0 => 1.19)
- added a new br on perl(Exporter) (version 0)
- added a new br on perl(Test) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.35-6
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.35-5
- rebuild for new perl

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 0.35-4
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 0.35-3
- Improve Summary, description, and Source0 URL.
- Fix find option ordering.
- Don't generate license texts.

* Fri Sep 16 2005 Steven Pritchard <steve@kspei.com> 0.35-2
- Minor spec cleanup.

* Sat Aug 27 2005 Steven Pritchard <steve@kspei.com> 0.35-1
- Specfile autogenerated.
