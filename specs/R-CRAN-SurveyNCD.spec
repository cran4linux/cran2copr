%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurveyNCD
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survey-Weighted Analysis of Self-Reported Health Indicators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-tidyr 

%description
Design-based analysis of population health survey data from the World
Health Organization (WHO) Stepwise Approach to Non-Communicable Disease
(NCD) Risk Factor Surveillance (STEPS), Demographic and Health Surveys
(DHS), Multiple Indicator Cluster Surveys (MICS) and similar complex
sample surveys, where chronic conditions are self-reported rather than
coded with the International Classification of Diseases (ICD). Provides
survey design constructors for DHS, MICS and STEPS microdata; design-based
prevalence for any binary indicators and groupings; a self-reported
multimorbidity count based on the Functional Comorbidity Index (FCI) of
Groll et al. (2005) <doi:10.1016/j.jclinepi.2004.10.018>, with
condition-pattern analysis, sensitivity bounds for missing answers, and
direct age standardisation to the WHO World Standard Population; standard,
generalized, Erreygers and Wagstaff concentration indices with
design-based standard errors following Kakwani, Wagstaff and van Doorslaer
(1997) <doi:10.1016/S0304-4076(96)01807-6> and O'Donnell et al. (2016)
<doi:10.1177/1536867X1601600112>, concentration curves, and slope and
relative indices of inequality; categorisation of DHS-coded child growth
z-scores; publication-ready tables and plots. Simulated example data with
a known population are included. Experimental helpers for choropleth maps
and case-weighted gradient boosting with SHapley Additive exPlanations
(SHAP) are also provided.

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
