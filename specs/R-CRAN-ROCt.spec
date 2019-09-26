%global packname  ROCt
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}
Summary:          Time-Dependent ROC Curve Estimators and Expected UtilityFunctions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-date 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-relsurv 
BuildRequires:    R-CRAN-timereg 
Requires:         R-splines 
Requires:         R-CRAN-date 
Requires:         R-survival 
Requires:         R-CRAN-relsurv 
Requires:         R-CRAN-timereg 

%description
Contains functions in order to estimate diagnostic and prognostic
capacities of continuous markers. More precisely, one function concerns
the estimation of time-dependent ROC (ROCt) curve, as proposed by Heagerty
et al. (2000) <doi:10.1111/j.0006-341X.2000.00337.x>. One function
concerns the adaptation of the ROCt theory for studying the capacity of a
marker to predict the excess of mortality of a specific population
compared to the general population. This last part is based on additive
relative survival models and the work of Pohar-Perme et al. (2012)
<doi:10.1111/j.1541-0420.2011.01640.x>. We also propose two functions for
cut-off estimation in medical decision making by maximizing time-dependent
expected utility function. Finally, we propose confounder-adjusted
estimators of ROC and ROCt curves by using the Inverse Probability
Weighting (IPW) approach.  For the confounder-adjusted ROC curve (without
censoring), we also proposed the implementation of the estimator based on
placement values proposed by Pepe and Cai (2004)
<doi:10.1111/j.0006-341X.2004.00200.x>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
