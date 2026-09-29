%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PFIM
%global packver   8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Population Fisher Information Matrix

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-S7 >= 0.2.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-tools 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-S7 >= 0.2.0
Requires:         R-utils 
Requires:         R-CRAN-Deriv 
Requires:         R-methods 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-knitr 
Requires:         R-tools 
Requires:         R-grDevices 

%description
Evaluate or optimize designs for nonlinear mixed effects models using the
Fisher Information matrix. Supports population, individual, and Bayesian
'FIMs', covariates, inter-occasion variability, and D-optimal search
('Fedorov-Wynn', multiplicative, simplex, 'PSO', 'PGBO').

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
