%global projname cran2copr
%global busname org.fedoraproject.%{projname}1
%global packname CoprManager
%global rlibdir %{_datadir}/R/library

Name:           R-%{packname}
Version:        0.1.0
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
%{_bindir}/R CMD build %{packname}

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}_%{version}.tar.gz
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

mkdir -p %{buildroot}%{_datadir}/dbus-1/system-services
mv %{buildroot}%{rlibdir}/%{packname}/service/%{busname}.service \
    %{buildroot}%{_datadir}/dbus-1/system-services
    
mkdir -p %{buildroot}%{_sysconfdir}/dbus-1/system.d
mv %{buildroot}%{rlibdir}/%{packname}/service/%{busname}.conf \
    %{buildroot}%{_sysconfdir}/dbus-1/system.d

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
