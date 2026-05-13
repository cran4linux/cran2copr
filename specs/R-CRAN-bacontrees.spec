%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bacontrees
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Context Trees for Discrete Sequence Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Brobdingnag 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Brobdingnag 

%description
Models discrete sequential data using Bayesian Context Trees. Context
trees, also known as Variable Length Markov Chains (VLMCs), are
parsimonious Markov models where the order of dependence can vary with the
observed past. Provides a generic 'R6' class structure that exposes the
full tree for building custom algorithms, exact Bayesian inference via a
bottom-up recursive algorithm (closed-form marginal likelihood, Maximum A
Posteriori (MAP) tree, exact posterior probabilities, and exact sampling
from the posterior), a frequentist estimator via the context algorithm
with likelihood-ratio pruning, simulation utilities, and a
Metropolis-Hastings sampler. See Paulichen and Freguglia (2026)
<doi:10.48550/arXiv.2603.25806>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
