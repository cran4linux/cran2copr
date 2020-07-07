%global packname  PLMIX
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}
Summary:          Bayesian Analysis of Finite Mixtures of Plackett-Luce Models forPartial Rankings/Orderings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gtools >= 3.8.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-label.switching >= 1.6
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-MCMCpack >= 1.4.2
BuildRequires:    R-CRAN-pmr >= 1.2.5
BuildRequires:    R-CRAN-ggmcmc >= 1.2
BuildRequires:    R-CRAN-rcdd >= 1.2
BuildRequires:    R-CRAN-rankdist >= 1.1.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-prefmod >= 0.8.34
BuildRequires:    R-CRAN-radarchart >= 0.3.1
BuildRequires:    R-CRAN-PlackettLuce >= 0.2.3
BuildRequires:    R-CRAN-coda >= 0.19.1
BuildRequires:    R-CRAN-StatRank >= 0.0.6
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-gtools >= 3.8.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-label.switching >= 1.6
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-MCMCpack >= 1.4.2
Requires:         R-CRAN-pmr >= 1.2.5
Requires:         R-CRAN-ggmcmc >= 1.2
Requires:         R-CRAN-rcdd >= 1.2
Requires:         R-CRAN-rankdist >= 1.1.3
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-prefmod >= 0.8.34
Requires:         R-CRAN-radarchart >= 0.3.1
Requires:         R-CRAN-PlackettLuce >= 0.2.3
Requires:         R-CRAN-coda >= 0.19.1
Requires:         R-CRAN-StatRank >= 0.0.6
Requires:         R-stats 
Requires:         R-utils 

%description
Fit finite mixtures of Plackett-Luce models for partial top
rankings/orderings within the Bayesian framework. It provides MAP point
estimates via EM algorithm and posterior MCMC simulations via Gibbs
Sampling. It also fits MLE as a special case of the noninformative
Bayesian analysis with vague priors. In addition to inferential
techniques, the package assists other fundamental phases of a model-based
analysis for partial rankings/orderings, by including functions for data
manipulation, simulation, descriptive summary, model selection and
goodness-of-fit evaluation. Main references on the methods are Mollica and
Tardella (2017) <doi.org/10.1007/s11336-016-9530-0> and Mollica and
Tardella (2014) <doi/10.1002/sim.6224>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
