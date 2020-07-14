%global projname bspm
%global packname CoprManager
%global rlibdir %{_datadir}/R/library

Name:           R-%{packname}
Version:        0.3.1
Release:        2%{?dist}
Summary:        Package Manager for the 'cran2copr' Project

License:        MIT
URL:            https://github.com/Enchufa2/%{projname}
Source0:        %{url}/archive/v%{version}/%{projname}_%{version}.tar.gz

BuildRequires:  R-devel
Requires:       systemd, python3-dbus, python3-gobject, python3-dnf
BuildArch:      noarch

%description
Enables binary package installations in Fedora systems based on
the 'cran2copr' project. Provides a installation function that talks over
D-Bus to a systemd service that manages package installations via DNF.

%prep
%setup -q -n %{projname}-%{version}

%build
rename %{projname} CoprManager inst/service/%{projname}.py
sed -i 's/%{projname}/CoprManager/' DESCRIPTION
sed -i 's/%{projname}/CoprManager/g' R/* inst/service/dbus.service.in
rename _sys _copr man/*
sed -i 's/_sys/_copr/g' NAMESPACE man/* R/*

cat <<EOF > inst/service/dbus-paths
OPATH="/org/fedoraproject/cran2copr1/PackageManager"
IFACE="org.fedoraproject.cran2copr1.PackageManager"
BUS_NAME="org.fedoraproject.cran2copr1"
EOF

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} . \
  --configure-vars="BUILD_ROOT=%{buildroot}" \
  --configure-vars="PKG_PREF='R-CRAN-'"
rm -f %{buildroot}%{rlibdir}/R.css

# enable by default
mkdir -p %{buildroot}%{_libdir}/R/etc
echo "suppressMessages(CoprManager::enable())" \
  > %{buildroot}%{_libdir}/R/etc/Rprofile.site

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/service
%{_datadir}/dbus-1/system-services/org.fedoraproject.cran2copr1.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.fedoraproject.cran2copr1.conf
%config %{_libdir}/R/etc/Rprofile.site

%changelog
