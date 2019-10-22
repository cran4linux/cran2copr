%global packname  riskRegression
%global packver   2019.01.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.01.29
Release:          1%{?dist}
Summary:          Risk Regression Models and Prediction Scores for SurvivalAnalysis with Competing Risks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-rms >= 5.0.0
BuildRequires:    R-survival >= 2.40.1
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-timereg >= 1.9.1
BuildRequires:    R-CRAN-prodlim >= 1.6.1
BuildRequires:    R-CRAN-lava >= 1.4.7
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rms >= 5.0.0
Requires:         R-survival >= 2.40.1
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-timereg >= 1.9.1
Requires:         R-CRAN-prodlim >= 1.6.1
Requires:         R-CRAN-lava >= 1.4.7
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-doParallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ranger 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 

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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
