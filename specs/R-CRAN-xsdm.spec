%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xsdm
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Demographic Approach to Species Distribution Model

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppParallel >= 5.1.10
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ucminfcpp 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.callr 
BuildRequires:    R-CRAN-sobol 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-RcppParallel >= 5.1.10
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-expm 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ucminfcpp 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.callr 
Requires:         R-CRAN-sobol 
Requires:         R-CRAN-purrr 

%description
Integrates concepts of stochastic demography into species distribution
modelling. The main approach maximizes a likelihood function based on
environmental information and presence/absence records. This is used to
reconstruct species' fundamental ecological niches and to project their
potential geographic range. Data requirements include species
presence/absence records and a timeseries of environmental data.

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
