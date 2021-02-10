%global packname  PandemicLP
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Long Term Prediction for Epidemic and Pandemic Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-plotly >= 4.9.2.1
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-plotly >= 4.9.2.1
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Implementation of the methodology described in
<http://est.ufmg.br/covidlp/home/pt/> which can be also found in
help(models). Implemented models are currently the Poisson distribution.
The mean function can be the basic generalized logistic form, or the
seasonal effect which has under- or over-reporting effects in up to three
weekdays, or the two curves form. Bayesian inference is made available
through the 'stan' software and its diagnostic functions pool can be used.
Plot methods are implemented to mimic the graphics from the 'shiny' app in
the URL using the 'plotly' library.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
