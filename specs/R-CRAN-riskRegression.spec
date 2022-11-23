%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  riskRegression
%global packver   2022.11.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2022.11.21
Release:          1%{?dist}%{?buildtag}
Summary:          Risk Regression Models and Prediction Scores for Survival Analysis with Competing Risks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rms >= 5.1.3
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-prodlim >= 2018.4.18
BuildRequires:    R-CRAN-survival >= 2.44.1
BuildRequires:    R-CRAN-timereg >= 1.9.3
BuildRequires:    R-CRAN-lava >= 1.6.5
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-mets 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-Publish 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rms >= 5.1.3
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-prodlim >= 2018.4.18
Requires:         R-CRAN-survival >= 2.44.1
Requires:         R-CRAN-timereg >= 1.9.3
Requires:         R-CRAN-lava >= 1.6.5
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-mets 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-Publish 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Implementation of the following methods for event history analysis. Risk
regression models for survival endpoints also in the presence of competing
risks are fitted using binomial regression based on a time sequence of
binary event status variables. A formula interface for the Fine-Gray
regression model and an interface for the combination of cause-specific
Cox regression models. A toolbox for assessing and comparing performance
of risk predictions (risk markers and risk prediction models). Prediction
performance is measured by the Brier score and the area under the ROC
curve for binary possibly time-dependent outcome. Inverse probability of
censoring weighting and pseudo values are used to deal with right censored
data. Lists of risk markers and lists of risk models are assessed
simultaneously. Cross-validation repeatedly splits the data, trains the
risk prediction models on one part of each split and then summarizes and
compares the performance across splits.

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
