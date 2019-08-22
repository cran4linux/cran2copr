%global packname  ARpLMEC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Fitting Autoregressive Censored Linear Mixed-Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lmec 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-Matrix 
Requires:         R-stats4 
Requires:         R-CRAN-gmm 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-lmec 
Requires:         R-CRAN-mnormt 

%description
It fits left, right or interval censored mixed-effects linear model with
autoregressive errors of order p using the EM algorithm. It provides
estimates, standard errors of the parameters and prediction of future
observations.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
