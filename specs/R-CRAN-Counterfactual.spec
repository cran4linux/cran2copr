%global packname  Counterfactual
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation and Inference Methods for Counterfactual Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
Requires:         R-CRAN-quantreg 
Requires:         R-survival 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 

%description
Implements the estimation and inference methods for counterfactual
analysis described in Chernozhukov, Fernandez-Val and Melly (2013)
<DOI:10.3982/ECTA10582> "Inference on Counterfactual Distributions,"
Econometrica, 81(6). The counterfactual distributions considered are the
result of changing either the marginal distribution of covariates related
to the outcome variable of interest, or the conditional distribution of
the outcome given the covariates. They can be applied to estimate quantile
treatment effects and wage decompositions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
