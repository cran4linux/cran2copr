%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthiar
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Quantifying and Monetizing Health Impacts Attributable to Exposure

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
This R package has been developed with a focus on air pollution and noise
but can applied to other exposures. The initial development has been
funded by the European Union project BEST-COST. Disclaimer: It is work in
progress and the developers are not liable for any calculation errors or
inaccuracies resulting from the use of this package. References (in
chronological order): WHO (2003a) "Assessing the environmental burden of
disease at national and local levels"
<https://www.who.int/publications/i/item/9241546204> (accessed October
2025); WHO (2003b) "Comparative quantification of health risks: Conceptual
framework and methodological issues" <doi:10.1186/1478-7954-1-1> (accessed
October 2025); Miller & Hurley (2003) "Life table methods for quantitative
impact assessments in chronic mortality" <doi:10.1136/jech.57.3.200>
(accessed October 2025); Steenland & Armstrong (2006) "An Overview of
Methods for Calculating the Burden of Disease Due to Specific Risk
Factors" <doi:10.1097/01.ede.0000229155.05644.43> (accessed October 2025);
Miller (2010) "Report on estimation of mortality impacts of particulate
air pollution in London"
<https://cleanair.london/app/uploads/CAL-098-Mayors-health-study-report-June-2010-1.pdf>
(accessed October 2025); WHO (2011) "Burden of disease from environmental
noise" <https://iris.who.int/items/723ab97c-5c33-4e3b-8df1-744aa5bc1c27>
(accessed October 2025); Jerrett et al. (2013) "Spatial Analysis of Air
Pollution and Mortality in California" <doi:10.1164/rccm.201303-0609OC>
(accessed October 2025); GBD 2019 Risk Factors Collaborators (2020)
"Global burden of 87 risk factors in 204 countries and territories,
1990–2019" <doi:10.1016/S0140-6736(20)30752-2> (accessed October 2025);
VanderWeele (2019) "Optimal Approximate Conversions of Odds Ratios and
Hazard Ratios to Risk Ratios" <doi: 10.1111/biom.13197> (accessed October
2025); WHO (2020) "Health impact assessment of air pollution: AirQ+ life
table manual"
<https://iris.who.int/bitstream/handle/10665/337683/WHO-EURO-2020-1559-41310-56212-eng.pdf?sequence=1>
(accessed October 2025); ETC HE (2022) "Health risk assessment of air
pollution and the impact of the new WHO guidelines"
<https://www.eionet.europa.eu/etcs/all-etc-reports> (accessed October
2025); Kim et al. (2022) "DALY Estimation Approaches: Understanding and
Using the Incidence-based Approach and the Prevalence-based Approach"
<doi:10.3961/jpmph.21.597> (accessed October 2025); Pozzer et al. (2022)
"Mortality Attributable to Ambient Air Pollution: A Review of Global
Estimates" <doi:10.1029/2022GH000711> (accessed October 2025); Teaching
group in EBM (2022) "Evidence-based medicine research helper"
<https://ebm-helper.cn/en/Conv/HR_RR.html> (accessed October 2025).

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
