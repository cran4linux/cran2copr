%global packname  DPWeibull
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}
Summary:          Dirichlet Process Weibull Mixture Model for Survival Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-binaryLogic 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-binaryLogic 

%description
Use Dirichlet process Weibull mixture model and dependent Dirichlet
process Weibull mixture model for survival data with and without competing
risks. Dirichlet process Weibull mixture model is used for data without
covariates and dependent Dirichlet process model is used for regression
data. The package is designed to handle exact/right-censored/
interval-censored observations without competing risks and
exact/right-censored observations for data with competing risks. Inside
each cluster of Dirichlet process, we assume a multiplicative effect of
covariates as in Cox model and Fine and Gray model. For wrapper of the
DPdensity function from the R package DPpackage (already archived by CRAN)
that uses the Low Information Omnibus prior, please check
(<https://github.com/mjmartens/DPdensity-wrapper-with-LIO-prior>).

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
%{rlibdir}/%{packname}/libs
