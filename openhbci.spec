Summary:	HBCI - HomeBanking Computer Interface
Name:		openhbci
Version:	0.9.13
Release:	0.1
License:	GPLv2
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/openhbci/%{name}-%{version}.tar.gz
#Source0-MD5:	725605239b260ba04c808a9a280d6e85
URL:		http://openhbci.sourceforge.net/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HBCI is a bank-independent online banking standard, developed by the
German Central Banking Committee ZKA (Zentraler Kredit-Ausschuss). It
is a publicly available specification that defines the communication
between online banking applications and the credit institutes'
servers. In Germany, roughly half of all banks offer online banking
through HBCI, which are approximately 2000 banks.

%package devel
Summary:	HBCI - HomeBanking Computer Interface - development files
Group:		Development/Libraries

%description devel
Development files for HBCI - HomeBanking Computer Interface.

%package static
Summary:	HBCI - HomeBanking Computer Interface - static libraries
Group:		Development/Libraries

%description static
Static libraries for HBCI - HomeBanking Computer Interface.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/*.la
%dir %{_libdir}/openhbci
%{_libdir}/openhbci/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
