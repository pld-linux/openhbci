Summary:	HBCI - HomeBanking Computer Interface
Summary(pl):	HBCI - komputerowy interfejs do HomeBankingu
Name:		openhbci
Version:	0.9.13
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/openhbci/%{name}-%{version}.tar.gz
#Source0-MD5:	725605239b260ba04c808a9a280d6e85
URL:		http://openhbci.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HBCI is a bank-independent online banking standard, developed by the
German Central Banking Committee ZKA (Zentraler Kredit-Ausschuss). It
is a publicly available specification that defines the communication
between online banking applications and the credit institutes'
servers. In Germany, roughly half of all banks offer online banking
through HBCI, which are approximately 2000 banks.

%description -l pl
HBCI (HomeBanking Computer Interface) to niezale¿ny od banku standard
przeprowadzania operacji bankowych online, rozwijany przez niemiecki
centralny komitet bankowy ZKA (Zentraler Kredit-Ausschuss). Jest to
publicznie dostêpna specyfikacja definiuj±ca komunikacjê pomiêdzy
aplikacjami bankowymi dzia³aj±cymi online i serwerami instytucji
kredytowych. W Niemczech z grubsza po³owa (oko³o 2000) wszystkich
banków oferuje operacje online poprzez HBCI.

%package devel
Summary:	HBCI - HomeBanking Computer Interface - development files
Summary(pl):	Pliki programistyczne do interfejsu HBCI
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for HBCI - HomeBanking Computer Interface.

%description devel -l pl
Pliki programistyczne dla HBCI - komputerowego interfejsu do
HomeBankingu.

%package static
Summary:	HBCI - HomeBanking Computer Interface - static libraries
Summary(pl):	Statyczne biblioteki HBCI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for HBCI - HomeBanking Computer Interface.

%description static -l pl
Statyczne biblioteki HBCI - komputerowego interfejsu do HomeBankingu.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/openhbci
%{_libdir}/openhbci/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
