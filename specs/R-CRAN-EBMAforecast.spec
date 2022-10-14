%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EBMAforecast
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Ensemble Bayesian Model Averaging Forecasts using Gibbs Sampling or EM-Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-separationplot 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-plyr 
Requires:         R-graphics 
Requires:         R-CRAN-separationplot 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-gtools 
Requires:         R-methods 

%description
Create forecasts from multiple predictions using ensemble Bayesian model
averaging (EBMA). EBMA models can be estimated using an expectation
maximization (EM) algorithm or as fully Bayesian models via Gibbs
sampling. The methods in this package are Montgomery, Hollenbach, and Ward
(2015) <doi:10.1016/j.ijforecast.2014.08.001> and Montgomery, Hollenbach,
and Ward (2012) <doi:10.1093/pan/mps002>.

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
