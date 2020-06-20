%global packname  CausalQueries
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Make, Update, and Query Binary Causal Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dagitty 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randomizr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-dagitty 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-CRAN-randomizr 
Requires:         R-CRAN-stringr 

%description
Users can declare binary causal models, update beliefs about causal types
given data and calculate arbitrary estimands.  Model definition makes use
of 'dagitty' functionality. Updating is implemented in 'stan'. The
approach used in 'CausalQueries' is a generalization of the 'biqq' models
described in "Mixing Methods: A Bayesian Approach" (Humphreys and Jacobs,
2015, <DOI:10.1017/S0003055415000453>). The conceptual extension makes use
of work on probabilistic causal models described in Pearl's Causality
(Pearl, 2009, <DOI:10.1017/CBO9780511803161>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
