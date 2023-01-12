%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  em
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generic EM Algorithm

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-plm 
Requires:         R-methods 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-magrittr 

%description
A generic function for running the Expectation-Maximization (EM) algorithm
within a maximum likelihood framework, based on Dempster, Laird, and Rubin
(1977) <doi:10.1111/j.2517-6161.1977.tb01600.x> is implemented. It can be
applied after a model fitting using R's existing functions and packages.

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
