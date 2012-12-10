%define name lft
%define version 3.1
%define release %mkrel 2

Summary:	Alternative traceroute tool for network (reverse) engineers
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:            http://pwhois.org/lft/
Source0:	%{name}-%{version}.tar.gz
Patch0:		lft-3.1-fix_install.patch
Patch1:		lft-3.1-fix_str_fmt.patch
Group:		Networking/Other
# http://pwhois.org/license.who
License:	VOSTROM Public License
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	whob = %{version}-%{release}

%description
LFT, short for Layer Four Traceroute, is a sort of 'traceroute'
that often works much faster (than the commonly-used Van Jacobson
method) and goes through many configurations of packet-filter
based firewalls. More importantly, LFT implements numerous other
features including AS number lookups, loose source routing,
netblock name lookups, et al.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0 -b .fix_install
%patch1 -p0 -b .fix_str_fmt

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

echo "lft is suid because it requires a access to a raw socket in order to send packet." > README.suid

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG README TODO README.suid
%attr(4755,root,root) %{_bindir}/lft
%{_bindir}/whob
%{_mandir}/man8/*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1-2mdv2011.0
+ Revision: 612732
- the mass rebuild of 2010.1 packages

* Fri Mar 05 2010 Jani Välimaa <wally@mandriva.org> 3.1-1mdv2010.1
+ Revision: 514473
- new version 3.1
- fix install (P0)
- fix str fmt (P1)

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.2-8mdv2010.0
+ Revision: 438503
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2-7mdv2009.1
+ Revision: 298273
- rebuilt against libpcap-1.0.0

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.2-6mdv2009.0
+ Revision: 248372
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.2-4mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import lft


* Tue Sep 12 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2-4mdv2007.0
- rebuild

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2-3mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Tue Jul 13 2004 Michael Scherer <misc@mandrake.org> 2.2-2mdk 
- rebuild
- clean provides
- rpmbuildupdate aware
- explain the suid

* Wed Jun 11 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.2-1mdk
- 2.2
- use the %%configure2_5x macro

* Thu Apr 10 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.1-1mdk
- 2.1
- misc spec file fixes

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.0-2mdk
- build release

* Sat Nov 30 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.0-1mdk
- initial cooker contrib, fixed the provided spec file
- added P0

* Mon Oct 28 2002 Florin Andrei <florin@sgi.com>
- first version
- v2.0-1
