%global __brp_check_rpaths %{nil}
%global packname  guix.install
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Install R Packages with GNU Guix

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RUnit 
Requires:         R-CRAN-RUnit 

%description
This 'R' package provides a single procedure guix.install(), which allows
users to install 'R' packages via 'Guix' right from within their running
'R' session.  If the requested 'R' package does not exist in 'Guix' at
this time, the package and all its missing dependencies will be imported
recursively and the generated package definitions will be written to
~/.Rguix/packages.scm.  This record of imported packages can be used later
to reproduce the environment, and to add the packages in question to a
proper 'Guix' channel (or 'Guix' itself). guix.install() not only supports
installing packages from CRAN, but also from Bioconductor or even
arbitrary 'git' or 'mercurial' repositories, replacing the need for
installation via 'devtools'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
