%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DPI
%global packver   2025.10-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Directed Prediction Index for Causal Inference from Observational Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-MASS 

%description
The Directed Prediction Index ('DPI') is a quasi-causal inference (causal
discovery) method for observational data designed to quantify the relative
endogeneity (relative dependence) of outcome (Y) versus predictor (X)
variables in regression models. By comparing the proportion of variance
explained (R-squared) between the Y-as-outcome model and the X-as-outcome
model while controlling for a sufficient number of possible confounders,
it can suggest a plausible (admissible) direction of influence from a more
exogenous variable (X) to a more endogenous variable (Y). Methodological
details are provided at <https://psychbruce.github.io/DPI/>. This package
also provides functions for data simulation and network analysis
(correlation, partial correlation, and Bayesian networks).

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
