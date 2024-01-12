%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DHS.rates
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Demographic Indicators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-crayon 

%description
Calculates key indicators such as fertility rates (Total Fertility Rate
(TFR), General Fertility Rate (GFR), and Age Specific Fertility Rate
(ASFR)) using Demographic and Health Survey (DHS) women/individual data,
childhood mortality probabilities and rates such as Neonatal Mortality
Rate (NNMR), Post-neonatal Mortality Rate (PNNMR), Infant Mortality Rate
(IMR), Child Mortality Rate (CMR), and Under-five Mortality Rate (U5MR),
and adult mortality indicators such as the Age Specific Mortality Rate
(ASMR), Age Adjusted Mortality Rate (AAMR), Age Specific Maternal
Mortality Rate (ASMMR), Age Adjusted Maternal Mortality Rate (AAMMR), Age
Specific Pregnancy Related Mortality Rate (ASPRMR), Age Adjusted Pregnancy
Related Mortality Rate (AAPRMR), Maternal Mortality Ratio (MMR) and
Pregnancy Related Mortality Ratio (PRMR). In addition to the indicators,
the 'DHS.rates' package estimates sampling errors indicators such as
Standard Error (SE), Design Effect (DEFT), Relative Standard Error (RSE)
and Confidence Interval (CI). The package is developed according to the
DHS methodology of calculating the fertility indicators and the childhood
mortality rates outlined in the "Guide to DHS Statistics" (Croft, Trevor
N., Aileen M. J. Marshall, Courtney K. Allen, et al. 2018,
<https://dhsprogram.com/Data/Guide-to-DHS-Statistics/index.cfm>) and the
DHS methodology of estimating the sampling errors indicators outlined in
the "DHS Sampling and Household Listing Manual" (ICF International 2012,
<https://dhsprogram.com/pubs/pdf/DHSM4/DHS6_Sampling_Manual_Sept2012_DHSM4.pdf>).

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
