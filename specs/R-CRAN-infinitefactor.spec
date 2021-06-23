%global __brp_check_rpaths %{nil}
%global packname  infinitefactor
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Infinite Factor Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 

%description
Sampler and post-processing functions for semi-parametric Bayesian
infinite factor models, motivated by the Multiplicative Gamma Shrinkage
Prior of Bhattacharya and Dunson (2011)
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3419391/>. Contains
component C++ functions for building samplers for linear and 2-way
interaction factor models using the multiplicative gamma and
Dirichlet-Laplace shrinkage priors. The package also contains post
processing functions to return matrices that display rotational ambiguity
to identifiability through successive application of orthogonalization
procedures and resolution of column label and sign switching. This package
was developed with the support of the National Institute of Environmental
Health Sciences grant 1R01ES028804-01.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
