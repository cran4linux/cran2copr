%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurveyNCD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survey-Weighted Analysis of Self-Reported Health Indicators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
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
Analyses population health survey data from the World Health Organization
(WHO) Stepwise Approach to Non-Communicable Disease (NCD) Risk Factor
Surveillance (STEPS), Demographic and Health Surveys (DHS), Multiple
Indicator Cluster Surveys (MICS), and similar complex sample surveys,
where chronic conditions are self-reported rather than coded using the
International Classification of Diseases (ICD) and estimates must account
for stratification, clustering, and sampling weights. Includes a
self-reported multimorbidity index based on the Functional Comorbidity
Index (FCI) described by Groll et al. (2005)
<doi:10.1016/j.jclinepi.2004.10.018>, design-weighted population
prevalence estimation via the 'survey' package, a survey-weighted
concentration index for health inequality analysis, a DHS anthropometric
z-score categoriser, a choropleth mapping helper, and exploratory
survey-weighted gradient boosting (via 'xgboost') with SHapley Additive
exPlanations (SHAP) based explainability. The gradient boosting component
applies case weights but does not yet propagate cluster and strata design
effects into variance estimates; it should be treated as exploratory
rather than as design-based inference.

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
