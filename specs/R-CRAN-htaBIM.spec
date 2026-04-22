%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  htaBIM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Budget Impact Modelling for Health Technology Assessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Implements a structured, reproducible framework for budget impact
modelling (BIM) in health technology assessment (HTA), following the ISPOR
Task Force guidelines (Sullivan et al. (2014)
<doi:10.1016/j.jval.2013.08.2291> and Mauskopf et al. (2007)
<doi:10.1111/j.1524-4733.2007.00187.x>). Provides functions for
epidemiology-driven population estimation, market share modelling with
flexible uptake dynamics, per-patient cost calculation across multiple
cost categories, multi-year budget projections, payer perspective
analysis, deterministic sensitivity analysis (DSA), and probabilistic
sensitivity analysis (PSA) via Monte Carlo simulation. Produces
submission-quality outputs including ISPOR-aligned summary tables,
scenario comparison tables, per-patient cost breakdowns, tornado diagrams,
PSA histograms, and text and HTML reports compatible with NICE, CADTH, and
EU-HTA dossier formats. Ships with an interactive 'shiny' dashboard built
on 'bslib' for point-and-click model building and exploration.

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
