%global projname bspm
%global packname CoprManager
%global rlibdir %{_datadir}/R/library

%global modulename %{packname}
%global selinuxtype targeted

Name:           R-%{packname}
Version:        0.4.2.3
Release:        1%{?dist}%{?buildtag}
Summary:        Package Manager for the 'cran2copr' Project

License:        MIT
URL:            https://github.com/Enchufa2/%{projname}
Source0:        %{url}/archive/v%{version}/%{projname}_%{version}.tar.gz

BuildRequires:  R-devel, python3-devel
Requires:       python3-dnf
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
Recommends:     /usr/bin/busctl, python3-dbus, python3-gobject
BuildArch:      noarch

%description
Enables binary package installations in Fedora systems based on
the 'cran2copr' project. Provides a installation function that talks over
D-Bus to a systemd service that manages package installations via DNF.

%package selinux
Summary:        SELinux module for %{packname}
BuildRequires:  selinux-policy-devel
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildArch:      noarch
%{?selinux_requires}

%description selinux
This package contains the SELinux policy module for %{name}.

%prep
%setup -q -n %{projname}-%{version}

%build
rm -rf inst/tinytest tests
rename %{projname} %{packname} man/* inst/service/%{projname}.py
sed -i 's/%{projname}/%{packname}/' DESCRIPTION
sed -i 's/%{projname}/%{packname}/g' man/* R/* inst/scripts/*
sed -i 's/%{projname}/%{packname}/g' inst/service/dbus.service.in
sed -i 's@Enchufa2/%{packname}@Enchufa2/%{projname}@g' man/* R/*
sed -i 's/_sys/_copr/g' NAMESPACE man/* R/* inst/scripts/*
# do not update cache every time the installer runs
sed -i '/update_cache/d' inst/service/backend/dnf.py

cat <<EOF > inst/service/dbus-paths
OPATH="/org/fedoraproject/cran2copr1/PackageManager"
IFACE="org.fedoraproject.cran2copr1.PackageManager"
BUS_NAME="org.fedoraproject.cran2copr1"
EOF

# selinux policy
mkdir selinux && echo "^selinux" >> .Rbuildignore
pushd selinux
  cat <<'  EOF' | sed -r 's/^ {2}//' > %{modulename}.te
  policy_module(%{modulename},%{version})
  require {
    type unconfined_t;
    type unconfined_service_t;
    class dir { add_name write };
  }
  allow unconfined_service_t unconfined_t:dir write;
  allow unconfined_service_t unconfined_t:dir add_name;
  EOF

  make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
  bzip2 -9 %{modulename}.pp
popd

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
cat <<EOF > %{buildroot}%{_libdir}/R/etc/Rprofile.site.d/50-%{packname}.site
options(%{packname}.sudo.autodetect=TRUE)
options(%{packname}.backend.check=FALSE)
suppressMessages(%{packname}::enable())
EOF
cat <<EOF > %{buildroot}%{_libdir}/R/etc/Rprofile.site
local({
  for (startup_file in Sys.glob(R.home("etc/Rprofile.site.d/*.site")))
    source(startup_file)
})
EOF

# selinux
install -D -m 0644 selinux/%{modulename}.pp.bz2 \
  %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
%selinux_modules_uninstall -s %{selinuxtype} %{modulename}

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files
# main
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
%{rlibdir}/%{packname}/scripts
# python service
%dir %{rlibdir}/%{packname}/service
%config %{rlibdir}/%{packname}/service/%{projname}.excl
%config %{rlibdir}/%{packname}/service/%{projname}.pref
%config %{rlibdir}/%{packname}/service/dbus-paths
%config %{rlibdir}/%{packname}/service/nodiscover
%{rlibdir}/%{packname}/service/%{packname}.py
%{rlibdir}/%{packname}/service/backend
# dbus files
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/org.fedoraproject.cran2copr1.service
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.fedoraproject.cran2copr1.conf
# Rprofile
%config(noreplace) %{_libdir}/R/etc/Rprofile.site
%dir %{_libdir}/R/etc/Rprofile.site.d
%config(noreplace) %{_libdir}/R/etc/Rprofile.site.d/50-%{packname}.site

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*

%changelog
