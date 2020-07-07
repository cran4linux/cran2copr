%global packname  EBMAforecast
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Estimate Ensemble Bayesian Model Averaging Forecasts using GibbsSampling or EM-Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-separationplot 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-plyr 
Requires:         R-graphics 
Requires:         R-CRAN-separationplot 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-gtools 
Requires:         R-methods 

%description
Create forecasts from multiple predictions using ensemble Bayesian model
averaging (EBMA). EBMA models can be estimated using an expectation
maximization (EM) algorithm or as fully Bayesian models via Gibbs
sampling.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/libs
