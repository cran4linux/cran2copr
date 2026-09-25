%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  campsisnca
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Compartmental Analysis for Campsis Simulation Platform

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-campsismod 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-campsis 
BuildRequires:    R-CRAN-cards 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-campsismod 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-campsis 
Requires:         R-CRAN-cards 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
A flexible and user-friendly non-compartmental analysis (NCA) toolkit
designed to work seamlessly with simulated pharmacokinetic data generated
using the 'campsis' ecosystem. The package provides a comprehensive
framework to compute standard and custom NCA metrics, including exposure
(AUC), peak/trough concentrations, half-life and time-above/below
thresholds, with support for configurable time windows and summary
statistics. 'campsisnca' integrates tightly with 'campsis' and
'campsismod', enabling streamlined workflows from simulation to analysis.
In addition, the package provides a JSON-based interface to define NCA
analyses, metrics and options using formal schemas, allowing analyses to
be created, validated and executed outside of R and facilitating
reproducibility, automation and system integration. The package also
includes utilities for generating formatted summary tables and exporting
results in multiple formats suitable for reporting. Trapezoidal rule
implementation for AUC calculation is based on the 'qpNCA' package by
Huisman, Jolling, Mehta and Bergsma (2021)
<doi:10.32614/CRAN.package.qpNCA>, following methodology from Rowland and
Tozer (2011, ISBN:978-0-683-07404-8). The package itself is licensed under
the GPL (>= 3); the JSON schema files shipped in inst/extdata are licensed
separately under the Creative Commons Attribution 4.0 International (CC BY
4.0).

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
