%global packname  Hmsc
%global packver   3.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.6
Release:          1%{?dist}
Summary:          Hierarchical Model of Species Communities

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-BayesLogit 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-MCMCpack 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nnet 
Requires:         R-CRAN-rlang 
Requires:         R-parallel 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-truncnorm 

%description
Hierarchical Modelling of Species Communities (HMSC) is a model-based
approach for analyzing community ecological data. This package implements
it in the Bayesian framework with Gibbs Markov chain Monte Carlo (MCMC)
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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.md
%{rlibdir}/%{packname}/INDEX
