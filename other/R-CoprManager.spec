%global projname bspm
%global packname CoprManager
%global rlibdir %{_datadir}/R/library

Name:           R-%{packname}
Version:        0.3.5
Release:        1%{?dist}%{?buildtag}
Summary:        Package Manager for the 'cran2copr' Project

License:        MIT
URL:            https://github.com/Enchufa2/%{projname}
Source0:        %{url}/archive/v%{version}/%{projname}_%{version}.tar.gz

BuildRequires:  R-devel, python3-devel
Requires:       systemd, python3-dbus, python3-gobject, python3-dnf
BuildArch:      noarch

%description
Enables binary package installations in Fedora systems based on
the 'cran2copr' project. Provides a installation function that talks over
D-Bus to a systemd service that manages package installations via DNF.

%prep
%setup -q -n %{projname}-%{version}

%build
rm -rf inst/tinytest tests
rename %{projname} %{packname} man/* inst/service/%{projname}.py
sed -i 's/%{projname}/%{packname}/' DESCRIPTION
sed -i 's/%{projname}/%{packname}/g' man/* R/* inst/service/dbus.service.in
sed -i 's@Enchufa2/%{packname}@Enchufa2/%{projname}@g' man/* R/*
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
rm -f %{buildroot}%{rlibdir}/%{packname}/service/*.in
%py_byte_compile %{python3} %{buildroot}%{rlibdir}/%{packname}/service/backend

# enable by default
mkdir -p %{buildroot}%{_libdir}/R/etc/Rprofile.site.d
echo "suppressMessages(%{packname}::enable())" \
  > %{buildroot}%{_libdir}/R/etc/Rprofile.site.d/50-%{packname}.site
cat <<EOF > %{buildroot}%{_libdir}/R/etc/Rprofile.site
local({
  for (startup_file in Sys.glob(R.home("etc/Rprofile.site.d/*.site")))
    source(startup_file)
})
EOF

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
%dir %{rlibdir}/%{packname}/service
%config %{rlibdir}/%{packname}/service/%{projname}.excl
%config %{rlibdir}/%{packname}/service/%{projname}.pref
%config %{rlibdir}/%{packname}/service/dbus-paths
%config %{rlibdir}/%{packname}/service/nodiscover
%{rlibdir}/%{packname}/service/%{packname}.py
%{rlibdir}/%{packname}/service/backend
%{_datadir}/dbus-1/system-services/org.fedoraproject.cran2copr1.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.fedoraproject.cran2copr1.conf
%config(noreplace) %{_libdir}/R/etc/Rprofile.site
%dir %{_libdir}/R/etc/Rprofile.site.d
%config(noreplace) %{_libdir}/R/etc/Rprofile.site.d/50-%{packname}.site

%changelog
