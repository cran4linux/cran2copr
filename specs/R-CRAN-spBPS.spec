%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spBPS
%global packver   0.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Predictive Stacking for Scalable Geospatial Transfer Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-mniw 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-mniw 

%description
Provides functions for Bayesian Predictive Stacking within the Bayesian
transfer learning framework for geospatial artificial systems, as
introduced in "Bayesian Transfer Learning for Artificially Intelligent
Geospatial Systems: A Predictive Stacking Approach" (Presicce and
Banerjee, 2024) <doi:10.48550/arXiv.2410.09504>. This methodology enables
efficient Bayesian geostatistical modeling, utilizing predictive stacking
to improve inference across spatial datasets. The core functions leverage
'C++' for high-performance computation, making the framework well-suited
for large-scale spatial data analysis in parallel and distributed
computing environments. Designed for scalability, it allows seamless
application in computationally demanding scenarios.

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
