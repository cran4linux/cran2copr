%global __brp_check_rpaths %{nil}
%global packname  mHMMbayes
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Multilevel Hidden Markov Models Using Bayesian Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 

%description
An implementation of the multilevel (also known as mixed or random
effects) hidden Markov model using Bayesian estimation in R. The
multilevel hidden Markov model (HMM) is a generalization of the well-known
hidden Markov model, for the latter see Rabiner (1989)
<doi:10.1109/5.18626>. The multilevel HMM is tailored to accommodate
(intense) longitudinal data of multiple individuals simultaneously, see
e.g., de Haan-Rietdijk et al. <doi:10.1080/00273171.2017.1370364>. Using a
multilevel framework, we allow for heterogeneity in the model parameters
(transition probability matrix and conditional distribution), while
estimating one overall HMM. The model can be fitted on multivariate data
with a categorical distribution, and include individual level covariates
(allowing for e.g., group comparisons on model parameters). Parameters are
estimated using Bayesian estimation utilizing the forward-backward
recursion within a hybrid Metropolis within Gibbs sampler. The package
also includes various visualization options, a function to simulate data,
and a function to obtain the most likely hidden state sequence for each
individual using the Viterbi algorithm.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
