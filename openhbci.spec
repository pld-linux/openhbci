Summary:	HBCI - HomeBanking Computer Interface
Summary(pl.UTF-8):	HBCI - komputerowy interfejs do HomeBankingu
Name:		openhbci
Version:	0.9.18
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/openhbci/%{name}-%{version}.tar.gz
# Source0-md5:	9ac3f63674f852a3cc523de43e9b517d
Patch0:		%{name}-plugins.patch
Patch1:		%{name}-path.patch
Patch2:		%{name}-am18.patch
URL:		http://openhbci.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gwenhywfar-devel >= 1.0.0
BuildRequires:	libstdc++-devel >= 3.0.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HBCI is a bank-independent online banking standard, developed by the
German Central Banking Committee ZKA (Zentraler Kredit-Ausschuss). It
is a publicly available specification that defines the communication
between online banking applications and the credit institutes'
servers. In Germany, roughly half of all banks offer online banking
through HBCI, which are approximately 2000 banks.

%description -l pl.UTF-8
HBCI (HomeBanking Computer Interface) to niezależny od banku standard
przeprowadzania operacji bankowych online, rozwijany przez niemiecki
centralny komitet bankowy ZKA (Zentraler Kredit-Ausschuss). Jest to
publicznie dostępna specyfikacja definiująca komunikację pomiędzy
aplikacjami bankowymi działającymi online i serwerami instytucji
kredytowych. W Niemczech z grubsza połowa (około 2000) wszystkich
banków oferuje operacje online poprzez HBCI.

%package devel
Summary:	HBCI - HomeBanking Computer Interface - development files
Summary(pl.UTF-8):	Pliki programistyczne do interfejsu HBCI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gwenhywfar-devel >= 1.0.0
Requires:	libstdc++-devel >= 3.0.0
Requires:	openssl-devel >= 0.9.7d

%description devel
Development files for HBCI - HomeBanking Computer Interface.

%description devel -l pl.UTF-8
Pliki programistyczne dla HBCI - komputerowego interfejsu do
HomeBankingu.

%package static
Summary:	HBCI - HomeBanking Computer Interface - static libraries
Summary(pl.UTF-8):	Statyczne biblioteki HBCI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for HBCI - HomeBanking Computer Interface.

%description static -l pl.UTF-8
Statyczne biblioteki HBCI - komputerowego interfejsu do HomeBankingu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-openssl-libs=%{_libdir} \
	--with-plugin-path=%{_libdir}/%{name}/plugins
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/openhbci/plugins/*/media/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libopenhbci.so.*.*.*
%dir %{_libdir}/openhbci
%dir %{_libdir}/openhbci/plugins
%dir %{_libdir}/openhbci/plugins/*
%dir %{_libdir}/openhbci/plugins/*/media
%attr(755,root,root) %{_libdir}/openhbci/plugins/*/media/rdhfile.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/openhbci-config
%attr(755,root,root) %{_libdir}/libopenhbci.so
%{_libdir}/libopenhbci.la
%{_includedir}/openhbci.h
%{_includedir}/openhbci
%{_aclocaldir}/openhbci.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenhbci.a
