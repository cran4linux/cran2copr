%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BCEA
%global packver   2.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Cost Effectiveness Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-cli >= 3.3.0
BuildRequires:    R-CRAN-voi >= 1.0.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MCMCvis 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-cli >= 3.3.0
Requires:         R-CRAN-voi >= 1.0.1
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MCMCvis 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rstantools

%description
Produces an economic evaluation of a sample of suitable variables of cost
and effectiveness / utility for two or more interventions, e.g. from a
Bayesian model in the form of MCMC simulations. This package computes the
most cost-effective alternative and produces graphical summaries and
probabilistic sensitivity analysis, see Baio et al (2017)
<doi:10.1007/978-3-319-55718-2>.

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
