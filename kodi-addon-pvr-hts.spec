%define		kodi_ver	20
%define		next_kodi_ver	%(echo $((%{kodi_ver}+1)))
%define		codename	Nexus
%define		addon		pvr.hts

Summary:	Kodi's Tvheadend HTSP client addon
Name:		kodi-addon-pvr-hts
Version:	%{kodi_ver}.6.2
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://github.com/kodi-pvr/pvr.hts/archive/%{version}-%{codename}/%{version}-%{codename}.tar.gz
# Source0-md5:	e3d7dfc3e42f0b6af581bf95b91a968c
URL:		https://github.com/kodi-pvr/pvr.hts
BuildRequires:	cmake >= 3.5
BuildRequires:	kodi-devel >= %{kodi_ver}
BuildRequires:	kodi-devel < %{next_kodi_ver}
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	kodi >= %{kodi_ver}
Requires:	kodi < %{next_kodi_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kodi's Tvheadend HTSP client addon.

%prep
%setup -q -n %{addon}-%{version}-%{codename}

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/kodi/addons/%{addon}
%attr(755,root,root) %{_libdir}/kodi/addons/%{addon}/%{addon}.so.%{version}
%dir %{_datadir}/kodi/addons/%{addon}
%{_datadir}/kodi/addons/%{addon}/addon.xml
%{_datadir}/kodi/addons/%{addon}/changelog.txt
%{_datadir}/kodi/addons/%{addon}/icon.png
%{_datadir}/kodi/addons/%{addon}/resources
