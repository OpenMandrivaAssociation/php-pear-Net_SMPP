%define		_class		Net
%define		_subclass	SMPP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	SMPP v3.4 protocol implementation
Name:		php-pear-%{_pearname}
Version:	0.4.4
Release:	%mkrel 4
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Net_SMPP is an implementation of the SMPP (Short Message Peer-to-Peer)
v3.4 protocol. SMPP is an open protocol used in the wireless industry
to send and recieve SMS messages.

Net_SMPP does not provide a SMPP client or server, but they can easily
be built with it.

In PEAR status of this package is: %{_status}.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT

install -d %buildroot%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/*.php %buildroot%{_datadir}/pear/%{_class}/
cp -fr  %{_pearname}-%{version}/SMPP/* %buildroot%{_datadir}/pear/%{_class}/%{_subclass}

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml
