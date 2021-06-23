%global __brp_check_rpaths %{nil}
%global packname  roben
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Bayesian Variable Selection for Gene-EnvironmentInteractions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 

%description
Gene-environment (G×E) interactions have important implications to
elucidate the etiology of complex diseases beyond the main genetic and
environmental effects. Outliers and data contamination in disease
phenotypes of G×E studies have been commonly encountered, leading to the
development of a broad spectrum of robust penalization methods.
Nevertheless, within the Bayesian framework, the issue has not been taken
care of in existing studies. We develop a robust Bayesian variable
selection method for G×E interaction studies. The proposed Bayesian method
can effectively accommodate heavy-tailed errors and outliers in the
response variable while conducting variable selection by accounting for
structural sparsity. In particular, the spike-and-slab priors have been
imposed on both individual and group levels to identify important main and
interaction effects. An efficient Gibbs sampler has been developed to
facilitate fast computation. The Markov chain Monte Carlo algorithms of
the proposed and alternative methods are efficiently implemented in C++.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
