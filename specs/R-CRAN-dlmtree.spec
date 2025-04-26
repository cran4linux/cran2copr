%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dlmtree
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Treed Distributed Lag Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-coda 

%description
Estimation of distributed lag models (DLMs) based on a Bayesian additive
regression trees framework. Includes several extensions of DLMs: treed
DLMs and distributed lag mixture models (Mork and Wilson, 2023)
<doi:10.1111/biom.13568>; treed distributed lag nonlinear models (Mork and
Wilson, 2022) <doi:10.1093/biostatistics/kxaa051>; heterogeneous DLMs
(Mork, et. al., 2024) <doi:10.1080/01621459.2023.2258595>; monotone DLMs
(Mork and Wilson, 2024) <doi:10.1214/23-BA1412>. The package also includes
visualization tools and a 'shiny' interface to check model convergence and
to help interpret results.

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
