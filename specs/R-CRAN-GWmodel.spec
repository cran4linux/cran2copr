%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GWmodel
%global packver   2.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Geographically-Weighted Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-sp > 1.4.0
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-spatialreg 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-sp > 1.4.0
Requires:         R-CRAN-robustbase 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-grDevices 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-spatialreg 
Requires:         R-CRAN-FNN 

%description
Techniques from a particular branch of spatial statistics,termed
geographically-weighted (GW) models. GW models suit situations when data
are not described well by some global model, but where there are spatial
regions where a suitably localised calibration provides a better
description. 'GWmodel' includes functions to calibrate: GW summary
statistics (Brunsdon et al., 2002)<doi: 10.1016/s0198-9715(01)00009-6>, GW
principal components analysis (Harris et al., 2011)<doi:
10.1080/13658816.2011.554838>, GW discriminant analysis (Brunsdon et al.,
2007)<doi: 10.1111/j.1538-4632.2007.00709.x> and various forms of GW
regression (Brunsdon et al., 1996)<doi:
10.1111/j.1538-4632.1996.tb00936.x>; some of which are provided in basic
and robust (outlier resistant) forms.

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
