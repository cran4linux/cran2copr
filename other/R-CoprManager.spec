%global projname cran2copr
%global busname org.fedoraproject.%{projname}1
%global packname CoprManager
%global rlibdir %{_datadir}/R/library

Name:           R-%{packname}
Version:        0.1.5
Release:        1%{?dist}
Summary:        Package Manager for the 'cran2copr' Project

License:        MIT
URL:            https://github.com/Enchufa2/cran2copr
Source0:        %{url}/archive/master.tar.gz#/%{projname}-master.tar.gz

BuildRequires:  R-devel
Requires:       systemd, python3-dbus, python3-gobject, python3-dnf
BuildArch:      noarch

%description
Enables binary package installations in Fedora systems based on
the 'cran2copr' project. Provides a installation function that talks over
D-Bus to a systemd service that manages package installations via DNF.

%prep
%setup -q -n %{projname}-master

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname} \
  --configure-vars="BUILD_DIR=%{buildroot}" \
  --configure-vars="DATA_DIR=%{buildroot}%{_datadir}" \
  --configure-vars="SYSCONF_DIR=%{buildroot}%{_sysconfdir}"
rm -f %{buildroot}%{rlibdir}/R.css

# enable by default
mkdir -p %{buildroot}%{_libdir}/R/etc
echo "suppressMessages(CoprManager::enable())" \
  > %{buildroot}%{_libdir}/R/etc/Rprofile.site

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/service
%{_datadir}/dbus-1/system-services/%{busname}.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/%{busname}.conf
%{_libdir}/R/etc/Rprofile.site

%changelog
