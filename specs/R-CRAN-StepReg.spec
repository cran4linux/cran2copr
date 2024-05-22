%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StepReg
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stepwise Regression Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-summarytools 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-summarytools 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjs 

%description
The stepwise regression analysis is a statistical technique used to
identify a subset of predictor variables essential for constructing
predictive models. This package performs stepwise regression analysis
across various regression models such as linear, logistic, Cox
proportional hazards, Poisson, Gamma, and negative binomial regression. It
incorporates diverse stepwise regression algorithms like forward
selection, backward elimination, and bidirectional elimination alongside
the best subset method. Additionally, it offers a wide range of selection
criteria, including Akaike Information Criterion (AIC), Sawa Bayesian
Information Criterion (BIC), and Significance Levels (SL). We validated
the output accuracy of StepReg using public datasets within the SAS
software environment. To facilitate efficient model comparison and
selection, StepReg allows for multiple strategies and selection metrics to
be executed in a single function call. Moreover, StepReg integrates a
Shiny application for interactive regression analysis, broadening its
accessibility.

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
