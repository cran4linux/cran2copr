%global packname  CovSelHigh
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Model-Free Covariate Selection in High Dimensions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-bindata 
BuildRequires:    R-CRAN-Matching 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-bartMachine 
BuildRequires:    R-CRAN-tmle 
Requires:         R-CRAN-bnlearn 
Requires:         R-MASS 
Requires:         R-CRAN-bindata 
Requires:         R-CRAN-Matching 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-bartMachine 
Requires:         R-CRAN-tmle 

%description
Model-free selection of covariates in high dimensions under
unconfoundedness for situations where the parameter of interest is an
average causal effect. This package is based on model-free backward
elimination algorithms proposed in de Luna, Waernbaum and Richardson
(2011) <DOI:10.1093/biomet/asr041> and VanderWeele and Shpitser (2011)
<DOI:10.1111/j.1541-0420.2011.01619.x>. Confounder selection can be
performed via either Markov/Bayesian networks, random forests or LASSO.

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
