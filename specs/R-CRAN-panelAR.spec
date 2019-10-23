%global packname  panelAR
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Estimation of Linear AR(1) Panel Data Models withCross-Sectional Heteroskedasticity and/or Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-car 

%description
The package estimates linear models on panel data structures in the
presence of AR(1)-type autocorrelation as well as panel heteroskedasticity
and/or contemporaneous correlation. First, AR(1)-type autocorrelation is
addressed via a two-step Prais-Winsten feasible generalized least squares
(FGLS) procedure, where the autocorrelation coefficients may be
panel-specific. A number of common estimators for the autocorrelation
coefficient are supported. In case of panel heteroskedasticty, one can
choose to use a sandwich-type robust standard error estimator with OLS or
a panel weighted least squares estimator after the two-step Prais-Winsten
estimator. Alternatively, if panels are both heteroskedastic and
contemporaneously correlated, the package supports panel-corrected
standard errors (PCSEs) as well as the Parks-Kmenta FGLS estimator.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
