%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HealthMarkers
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for Clinical, Metabolic, and Cardiovascular Biomarker Calculations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-Rdpack 

%description
Computes over 50 specialist health marker functions covering insulin
sensitivity and resistance indices (fasting, oral glucose tolerance test,
adipose-tissue, tracer, and dual-energy X-ray absorptiometry (DXA)-based),
glycaemic and lipid markers, atherogenic and metabolic syndrome scores,
liver steatosis and fibrosis scores, and cardiovascular risk algorithms
(Framingham Heart Study equations, atherosclerotic cardiovascular disease
(ASCVD) Pooled Cohort Equations, the QRISK3 cardiac risk score, and
Systematic Coronary Risk Evaluation 2 (SCORE2) including the Older Persons
variant (SCORE2-OP)). Also implements renal function (estimated glomerular
filtration rate (eGFR), Kidney Failure Risk Equation (KFRE), chronic
kidney disease (CKD) staging), pulmonary function (spirometry z-scores,
Body-mass index, airflow Obstruction, Dyspnea, and Exercise capacity index
(BODE)), inflammatory markers and the inflammatory age clock (iAge),
hormonal panels, body composition and anthropometric z-scores, bone
turnover markers and fracture risk (Fracture Risk Assessment Tool (FRAX)),
frailty and comorbidity indices (Rockwood, Charlson), psychiatric rating
scales, and biomarker panels from alternative biofluids (urine, saliva,
sweat). Missing value imputation helpers, pre or post computation
normalization and a unified all_health_markers() dispatcher that returns
all requested marker groups as a single wide tibble are included.

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
