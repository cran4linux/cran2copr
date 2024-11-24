%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multilevelcoda
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Bayesian Multilevel Models for Compositional Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-extraoperators 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinystan 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-posterior 
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-stats 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-extraoperators 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinystan 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-posterior 

%description
Implement Bayesian Multilevel Modelling for compositional data in a
multilevel framework. Compute multilevel compositional data and Isometric
log ratio (ILR) at between and within-person levels, fit Bayesian
multilevel models for compositional predictors and outcomes, and run
post-hoc analyses such as isotemporal substitution models. References: Le,
Stanford, Dumuid, and Wiley (2024) <doi:10.48550/arXiv.2405.03985>, Le,
Dumuid, Stanford, and Wiley (2024) <doi:10.48550/arXiv.2411.12407>.

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
