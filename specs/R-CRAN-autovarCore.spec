%global packname  autovarCore
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Automated Vector Autoregression Models and Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-vars 
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-jsonlite 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-vars 

%description
Automatically find the best vector autoregression models and networks for
a given time series data set. 'AutovarCore' evaluates eight kinds of
models: models with and without log transforming the data, lag 1 and lag 2
models, and models with and without weekday dummy variables. For each of
these 8 model configurations, 'AutovarCore' evaluates all possible
combinations for including outlier dummies (at 2.5x the standard deviation
of the residuals) and retains the best model. Model evaluation includes
the Eigenvalue stability test and a configurable set of residual tests.
These eight models are further reduced to four models because
'AutovarCore' determines whether adding weekday dummies improves the model
fit.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bash
%doc %{rlibdir}/%{packname}/docs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
