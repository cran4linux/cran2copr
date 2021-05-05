%global packname  geojsonR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A GeoJson Processing Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-R6 

%description
Includes functions for processing GeoJson objects
<https://en.wikipedia.org/wiki/GeoJSON> relying on 'RFC 7946'
<https://tools.ietf.org/pdf/rfc7946.pdf>. The geojson encoding is based on
'json11', a tiny JSON library for 'C++11'
<https://github.com/dropbox/json11>. Furthermore, the source code is
exported in R through the 'Rcpp' and 'RcppArmadillo' packages.

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
