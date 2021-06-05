%global packname  earthtide
%global packver   0.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Implementation of 'ETERNA 3.40' for Prediction and Analysis of Earth Tides

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 4.4.2
BuildRequires:    R-CRAN-R6 >= 2.3.0
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.200.7.0
Requires:         R-CRAN-RcppParallel >= 4.4.2
Requires:         R-CRAN-R6 >= 2.3.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
This is a port of 'Fortran ETERNA 3.4'
<http://igets.u-strasbg.fr/soft_and_tool.php> by H.G. Wenzel for
calculating synthetic Earth tides using the Hartmann and Wenzel (1994)
<doi:10.1029/95GL03324> or Kudryavtsev (2004)
<doi:10.1007/s00190-003-0361-2> tidal catalogs.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
