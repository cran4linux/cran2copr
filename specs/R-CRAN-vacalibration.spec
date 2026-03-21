%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vacalibration
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calibration of Computer-Coded Verbal Autopsy Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-openVA 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-openVA 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rstantools

%description
Calibrates population-level cause-specific mortality fractions (CSMFs)
that are derived using computer-coded verbal autopsy (CCVA) algorithms.
Leveraging the data collected in the Child Health and Mortality Prevention
Surveillance (CHAMPS;<https://champshealth.org/>) project, the package
stores misclassification matrix estimates of three CCVA algorithms (EAVA,
InSilicoVA, and InterVA) and two age groups (neonates aged 0-27 days, and
children aged 1-59 months) across countries (specific estimates for
Bangladesh, Ethiopia, Kenya, Mali, Mozambique, Sierra Leone, and South
Africa, and a combined estimate for all other countries), enabling global
calibration. These estimates are obtained using the framework proposed in
Pramanik et al. (2025;<doi:10.1214/24-AOAS2006>) and are analyzed in
Pramanik et al. (2026;<doi:10.1136/bmjgh-2025-021747>). Given VA-only data
for an age group, CCVA algorithm, and country, the package utilizes the
corresponding misclassification matrix estimate in the modular
VA-Calibration framework (Pramanik et al.,2025;<doi:10.1214/24-AOAS2006>)
and produces calibrated estimates of CSMFs. The package also supports
ensemble calibration to accommodate multiple algorithms. More generally,
this allows calibration of population-level prevalence derived from
single-class predictions of discrete classifiers. For this, users need to
provide fixed or uncertainty-quantified misclassification matrices. This
work is supported by the Eunice Kennedy Shriver National Institute of
Child Health K99 NIH Pathway to Independence Award (1K99HD114884-01A1),
the Bill and Melinda Gates Foundation (INV-034842), and the Johns Hopkins
Data Science and AI Institute.

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
