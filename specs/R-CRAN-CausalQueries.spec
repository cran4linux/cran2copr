%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CausalQueries
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Make, Update, and Query Binary Causal Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats >= 4.1.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-ggraph >= 2.2.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-knitr >= 1.45
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.1
BuildRequires:    R-CRAN-latex2exp >= 0.9.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-dirmult >= 0.1.3.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rstantools
Requires:         R-stats >= 4.1.1
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-ggraph >= 2.2.0
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-knitr >= 1.45
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-lifecycle >= 1.0.1
Requires:         R-CRAN-latex2exp >= 0.9.4
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-dirmult >= 0.1.3.4
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rstantools

%description
Users can declare causal models over binary nodes, update beliefs about
causal types given data, and calculate arbitrary queries.  Updating is
implemented in 'stan'. See Humphreys and Jacobs, 2023, Integrated
Inferences (<DOI: 10.1017/9781316718636>) and Pearl, 2009 Causality
(<DOI:10.1017/CBO9780511803161>).

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
