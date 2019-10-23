%global packname  spinBayes
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Semi-Parametric Gene-Environment Interaction via BayesianVariable Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-splines 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-splines 
Requires:         R-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-utils 

%description
Many complex diseases are known to be affected by the interactions between
genetic variants and environmental exposures beyond the main genetic and
environmental effects. Existing Bayesian methods for gene-environment
(G×E) interaction studies are challenged by the high-dimensional nature of
the study and the complexity of environmental influences. We have
developed a novel and powerful semi-parametric Bayesian variable selection
method that can accommodate linear and nonlinear G×E interactions
simultaneously (Ren et al. (2019) <arXiv:1906.01057>). Furthermore, the
proposed method can conduct structural identification by distinguishing
nonlinear interactions from main effects only case within Bayesian
framework. Spike-and-slab priors are incorporated on both individual and
group level to shrink coefficients corresponding to irrelevant main and
interaction effects to zero exactly. The Markov chain Monte Carlo
algorithms of the proposed and alternative methods are efficiently
implemented in C++.

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
