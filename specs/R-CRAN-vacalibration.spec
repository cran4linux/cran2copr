%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vacalibration
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calibration of Computer-Coded Verbal Autopsy Algorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rstantools

%description
Calibrates cause-specific mortality fractions (CSMF) estimates generated
by computer-coded verbal autopsy (CCVA) algorithms from WHO-standardized
verbal autopsy (VA) survey data. It leverages data from the multi-country
Child Health and Mortality Prevention Surveillance (CHAMPS) project
<https://champshealth.org/>, which determines gold standard causes of
death via Minimally Invasive Tissue Sampling (MITS). By modeling the
CHAMPS data using the misclassification matrix modeling framework proposed
in Pramanik et al. (2025, <doi:10.1214/24-AOAS2006>), the package includes
an inventory of 48 uncertainty-quantified misclassification matrices for
three CCVA algorithms (EAVA, InSilicoVA, InterVA), two age groups
(neonates aged 0-27 days and children aged 1-59 months), and eight
"countries" (seven countries in CHAMPS -- Bangladesh, Ethiopia, Kenya,
Mali, Mozambique, Sierra Leone, South Africa -- and an estimate for
countries not in CHAMPS). Given a VA-only data for an age group, CCVA
algorithm, and country, the package uses the corresponding
uncertainty-quantified misclassification matrix estimates as an
informative prior, and utilizes the modular VA-calibration to produce
calibrated CSMF estimates. It also supports ensemble calibration when
VA-only data are provided for multiple algorithms. More generally, the
package can be applied to calibrate predictions from a discrete classifier
(or ensemble of classifiers) utilizing user-provided fixed or
uncertainty-quantified misclassification matrices. This work is supported
by the Bill and Melinda Gates Foundation Grant INV-034842.

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
