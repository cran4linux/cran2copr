%global packname  JointAI
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}
Summary:          Joint Analysis and Imputation of Incomplete Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-MASS 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Provides joint analysis and imputation of (generalized) linear and
cumulative logit regression models, (generalized) linear and cumulative
logit mixed models and parametric (Weibull) as well as Cox proportional
hazards survival models with incomplete (covariate) data in the Bayesian
framework. The package performs some preprocessing of the data and creates
a 'JAGS' model, which will then automatically be passed to 'JAGS'
<http://mcmc-jags.sourceforge.net> with the help of the package 'rjags'.
It also provides summary and plotting functions for the output and allows
the user to export imputed values.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
