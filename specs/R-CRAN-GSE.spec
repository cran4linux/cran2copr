%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GSE
%global packver   4.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Estimation in the Presence of Cellwise and Casewise Contamination and Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.10.0
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
Robust Estimation of Multivariate Location and Scatter in the Presence of
Cellwise and Casewise Contamination and Missing Data.

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
