%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ParCC
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parameter Converter and Calculator for Health Technology Assessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-magrittr 

%description
An interactive 'shiny' application for Health Technology Assessment (HTA)
parameter estimation. Converts between rates, probabilities, odds, and
hazard ratios (HR); extrapolates survival curves (Exponential, Weibull,
Log-Logistic); fits probabilistic sensitivity analysis (PSA) distributions
(Beta, Gamma, LogNormal, Dirichlet) via the method of moments; calculates
incremental cost-effectiveness ratios (ICERs), net monetary benefit (NMB),
value-based pricing, and budget impact; adjusts costs for inflation,
discounting, and purchasing power parity (PPP) across 30 countries; and
adjusts background mortality using life-table methods. Designed for
researchers building cost-effectiveness and budget-impact models who need
auditable, formula-documented parameter transformations. Methods include
Zhang and Yu (1998) <doi:10.1001/jama.280.19.1690> for odds ratio (OR) to
relative risk (RR) conversion and Chinn (2000, Statistics in Medicine, 19,
3127-3131) for effect-size transformations.

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
