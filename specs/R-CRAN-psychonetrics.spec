%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psychonetrics
%global packver   0.11.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.5
Release:          1%{?dist}%{?buildtag}
Summary:          Structural Equation Modeling and Confirmatory Network Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-VCA 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-IsingSampler 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-pbv 
BuildRequires:    R-CRAN-roptim 
Requires:         R-methods 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-VCA 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-IsingSampler 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-rlang 

%description
Multi-group (dynamical) structural equation models in combination with
confirmatory network models from cross-sectional, time-series and panel
data <doi:10.31234/osf.io/8ha93>. Allows for confirmatory testing and fit
as well as exploratory model search.

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
