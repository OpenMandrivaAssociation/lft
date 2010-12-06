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
