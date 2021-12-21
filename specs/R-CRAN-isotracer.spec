%global __brp_check_rpaths %{nil}
%global packname  isotracer
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Isotopic Tracer Analysis Using MCMC

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-rstan >= 2.19.3
BuildRequires:    R-CRAN-StanHeaders >= 2.19.2
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.72.0
BuildRequires:    R-CRAN-pillar >= 1.4.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-latex2exp >= 0.4.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.7.0
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-coda >= 0.19.3
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rstantools
Requires:         R-methods >= 3.6.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-rstan >= 2.19.3
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-pillar >= 1.4.3
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-latex2exp >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-coda >= 0.19.3
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rstantools

%description
Implements Bayesian models to analyze data from tracer addition
experiments. The implemented method was originally described in the
article "A New Method to Reconstruct Quantitative Food Webs and Nutrient
Flows from Isotope Tracer Addition Experiments" by López-Sepulcre et al.
(2020) <doi:10.1086/708546>.

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
