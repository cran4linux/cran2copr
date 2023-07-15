%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PSS.Health
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Power and Sample Size for Health Researchers via Shiny

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-easypower 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-epiR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ICC.Sample.Size 
BuildRequires:    R-CRAN-kappaSize 
BuildRequires:    R-CRAN-longpower 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-powerMediation 
BuildRequires:    R-CRAN-powerSurvEpi 
BuildRequires:    R-CRAN-presize 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-pwr2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyFeedback 
BuildRequires:    R-CRAN-shinyhelper 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-easypower 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-epiR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ICC.Sample.Size 
Requires:         R-CRAN-kappaSize 
Requires:         R-CRAN-longpower 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-powerMediation 
Requires:         R-CRAN-powerSurvEpi 
Requires:         R-CRAN-presize 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-pwr2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyFeedback 
Requires:         R-CRAN-shinyhelper 
Requires:         R-CRAN-writexl 

%description
Power and Sample Size for Health Researchers is a Shiny application that
brings together a series of functions related to sample size and power
calculations for common analysis in the healthcare field. There are
functionalities to calculate the power, sample size to estimate or test
hypotheses for means and proportions (including test for correlated
groups, equivalence, non-inferiority and superiority), association,
correlations coefficients, regression coefficients (linear, logistic,
gamma, and Cox), linear mixed model, Cronbach's alpha, interobserver
agreement, intraclass correlation coefficients, limit of agreement on
Bland-Altman plots, area under the curve, sensitivity and specificity
incorporating the prevalence of disease. You can also use the online
version at <https://hcpa-unidade-bioestatistica.shinyapps.io/PSS_Health/>.

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
