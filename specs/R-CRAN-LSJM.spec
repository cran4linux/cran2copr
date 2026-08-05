%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LSJM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Location-Scale Joint Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-marqLevAlg 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-spacefillr 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-SmoothHazard 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-marqLevAlg 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-ggplot2 
Requires:         R-splines 
Requires:         R-CRAN-spacefillr 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-SmoothHazard 
Requires:         R-parallel 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 

%description
Estimation of mixed models including a subject-specific variance that can
be time- and covariate-dependent or defined for within- and between-visit
variability. In the joint modeling framework, the package handles left
truncation, interval censoring, and multistate models, and allows a
flexible dependence structure between competing events and the
longitudinal marker. Estimation is performed in a frequentist framework
using the Marquardt-Levenberg algorithm. Methods are described in Courcoul
et al. (2025) <doi:10.1002/sim.70244> and in Courcoul et al. (2026)
<doi:10.1002/bimj.70123>.

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
