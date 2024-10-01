%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pMEM
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Moran's Eigenvector Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-sf 

%description
Calculation of Predictive Moran's eigenvector maps (pMEM), as defined by
Guénard and Legendre (In Press) "Spatially-explicit predictions using
spatial eigenvector maps" <doi:10.5281/zenodo.13356457>. Methods in
Ecology and Evolution. This method enables scientists to predict the
values of spatially-structured environmental variables. Multiple types of
pMEM are defined, each one implemented on the basis of spatial weighting
function taking a range parameter, and sometimes also a shape parameter.
The code's modular nature enables programers to implement new pMEM by
defining new spatial weighting functions.

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
