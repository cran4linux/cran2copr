%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  egfr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimated Glomerular Filtration Rate (eGFR) Calculators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch

%description
A comprehensive, vectorised toolkit for estimating glomerular filtration
rate (eGFR) and creatinine clearance from serum creatinine, cystatin C, or
both. Implements adult, paediatric, and neonatal equations, including the
Chronic Kidney Disease Epidemiology Collaboration (CKD-EPI) equations
(2009, 2012, 2021), the Modification of Diet in Renal Disease (MDRD) Study
equation, Cockcroft-Gault, the European Kidney Function Consortium (EKFC)
equations, the Full Age Spectrum (FAS) equations, the Lund-Malmoe
equations, the Berlin Initiative Study (BIS) equations, the Schwartz
bedside equation, the Chronic Kidney Disease in Children Under 25 (CKiD
U25) equations, the Caucasian, Asian, Paediatric, and Adult (CAPA)
cystatin C equation, and a neonatal equation. Helpers for body surface
area, chronic kidney disease (CKD) staging following the Kidney Disease:
Improving Global Outcomes (KDIGO) guideline, and unit conversions are
included. Methods are described in Levey et al. (2009)
<doi:10.7326/0003-4819-150-9-200905050-00006>, Inker et al. (2021)
<doi:10.1056/NEJMoa2102953>, and Pottel et al. (2021)
<doi:10.7326/M20-4366>. Inspired by the 'kidney.epi' package.

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
