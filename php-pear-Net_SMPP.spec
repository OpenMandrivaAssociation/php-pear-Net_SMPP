%define		_class		Net
%define		_subclass	SMPP
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.4.5
Release:	4
Summary:	SMPP v3.4 protocol implementation
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires: php-pear
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Net_SMPP is an implementation of the SMPP (Short Message Peer-to-Peer)
v3.4 protocol. SMPP is an open protocol used in the wireless industry
to send and recieve SMS messages.

Net_SMPP does not provide a SMPP client or server, but they can easily
be built with it.

%prep
%setup -qc
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.5-2mdv2012.0
+ Revision: 741797
- fix major breakage by careless packager

* Thu Dec 15 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.5-1
+ Revision: 741529
- 0.4.5

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-7
+ Revision: 679493
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-6mdv2011.0
+ Revision: 613736
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.4-5mdv2010.1
+ Revision: 468718
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4.4-4mdv2010.0
+ Revision: 441492
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-3mdv2009.1
+ Revision: 322497
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.4.4-2mdv2009.0
+ Revision: 268960
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 0.4.4-1mdv2009.0
+ Revision: 216774
- import php-pear-Net_SMPP


