%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggdmc
%global packver   0.2.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Cognitive Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.100.3.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixStats 

%description
Hierarchical Bayesian models. The package provides tools to fit two
response time models, using the population-based Markov Chain Monte Carlo.

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
