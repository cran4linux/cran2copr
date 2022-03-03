%global __brp_check_rpaths %{nil}
%global packname  shinystan
%global packver   2.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Visual and Numerical Diagnostics and Posterior Analysis for Bayesian Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.17.1
BuildRequires:    R-CRAN-ggplot2 >= 2.1.1
BuildRequires:    R-CRAN-bayesplot >= 1.5.0
BuildRequires:    R-CRAN-dygraphs >= 1.1.1.2
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-shinythemes >= 1.0.1
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-markdown >= 0.7
BuildRequires:    R-CRAN-shinyjs >= 0.6.0
BuildRequires:    R-CRAN-threejs >= 0.2.1
BuildRequires:    R-CRAN-DT >= 0.2
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.17.1
Requires:         R-CRAN-ggplot2 >= 2.1.1
Requires:         R-CRAN-bayesplot >= 1.5.0
Requires:         R-CRAN-dygraphs >= 1.1.1.2
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-shinythemes >= 1.0.1
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-markdown >= 0.7
Requires:         R-CRAN-shinyjs >= 0.6.0
Requires:         R-CRAN-threejs >= 0.2.1
Requires:         R-CRAN-DT >= 0.2
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-rstantools

%description
A graphical user interface for interactive Markov chain Monte Carlo (MCMC)
diagnostics and plots and tables helpful for analyzing a posterior sample.
The interface is powered by the 'Shiny' web application framework from
'RStudio' and works with the output of MCMC programs written in any
programming language (and has extended functionality for 'Stan' models fit
using the 'rstan' and 'rstanarm' packages).

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
