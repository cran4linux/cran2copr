%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiModel
%global packver   2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mathematical Modeling of Infectious Disease Dynamics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-ergm >= 4.7.1
BuildRequires:    R-CRAN-tergm >= 4.2.1
BuildRequires:    R-CRAN-statnet.common >= 4.10.0
BuildRequires:    R-CRAN-deSolve >= 1.21
BuildRequires:    R-CRAN-network >= 1.18.1
BuildRequires:    R-CRAN-networkLite >= 1.0.5
BuildRequires:    R-CRAN-networkDynamic >= 0.11.3
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-collections 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ergm >= 4.7.1
Requires:         R-CRAN-tergm >= 4.2.1
Requires:         R-CRAN-statnet.common >= 4.10.0
Requires:         R-CRAN-deSolve >= 1.21
Requires:         R-CRAN-network >= 1.18.1
Requires:         R-CRAN-networkLite >= 1.0.5
Requires:         R-CRAN-networkDynamic >= 0.11.3
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-collections 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-coda 

%description
Tools for simulating mathematical models of infectious disease dynamics.
Epidemic model classes include deterministic compartmental models,
stochastic individual-contact models, and stochastic network models.
Network models use the robust statistical methods of exponential-family
random graph models (ERGMs) from the Statnet suite of software packages in
R. Standard templates for epidemic modeling include SI, SIR, and SIS
disease types. EpiModel features an API for extending these templates to
address novel scientific research aims. Full methods for EpiModel are
detailed in Jenness et al. (2018, <doi:10.18637/jss.v084.i08>).

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
