%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigergm
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fit, Simulate, and Diagnose Hierarchical Exponential-Family Models for Big Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ergm >= 4.5.0
BuildRequires:    R-CRAN-network >= 1.16.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-statnet.common 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-ergm.multi 
Requires:         R-CRAN-ergm >= 4.5.0
Requires:         R-CRAN-network >= 1.16.0
Requires:         R-CRAN-RcppArmadillo >= 0.10.5
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-statnet.common 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-intergraph 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-ergm.multi 

%description
A toolbox for analyzing and simulating large networks based on
hierarchical exponential-family random graph models (HERGMs).'bigergm'
implements the estimation for large networks efficiently building on the
'lighthergm' and 'hergm' packages. Moreover, the package contains tools
for simulating networks with local dependence to assess the
goodness-of-fit.

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
