%define name lft
%define version 2.2
%define release %mkrel 6

Summary:	Alternative traceroute tool for network (reverse) engineers
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://mainnerve.com/lft/%{name}-%{version}.tar.bz2
Group:		Networking/Other
URL:		http://www.mainnerve.com/lft/
License:	GPL
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
LFT, short for Layer Four Traceroute, is a sort of 'traceroute'
that often works much faster (than the commonly-used Van Jacobson
method) and goes through many configurations of packet-filter
based firewalls. More importantly, LFT implements numerous other
features including AS number lookups, loose source routing,
netblock name lookups, et al.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf "%{buildroot}"

#%%makeinstall

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8
install -m4755 lft %{buildroot}%{_bindir}/
install -m644 lft.8 %{buildroot}%{_mandir}/man8/

echo "lft is suid because it requires a access to a raw socket in order to send packet." > README.suid
%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc CHANGELOG README TODO lft-manpage.html README.suid
%{_bindir}/lft
%{_mandir}/man8/lft.8*

