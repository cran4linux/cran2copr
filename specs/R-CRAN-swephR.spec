%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  swephR
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          High Precision Swiss Ephemeris

License:          AGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
The Swiss Ephemeris (version 2.10.03) is a high precision ephemeris based
upon the DE431 ephemerides from NASA's JPL. It covers the time range 13201
BCE to 17191 CE. This package uses the semi-analytic theory by Steve
Moshier. For faster and more accurate calculations, the compressed Swiss
Ephemeris data is available in the 'swephRdata' package. To access this
data package, run 'install.packages("swephRdata", repos =
"https://rstub.r-universe.dev", type = "source")'. The size of the
'swephRdata' package is approximately 115 MB. The user can also use the
original JPL DE431 data.

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
