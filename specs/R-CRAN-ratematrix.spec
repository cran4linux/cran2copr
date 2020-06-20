%global packname  ratematrix
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Bayesian Estimation of the Evolutionary Rate Matrix

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-phylolm 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-mvMORPH 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-corpcor 
Requires:         R-MASS 
Requires:         R-CRAN-phylolm 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-mvMORPH 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ellipse 

%description
Estimates the evolutionary rate matrix (R) using Markov chain Monte Carlo
(MCMC) as described in Caetano and Harmon (2017)
<doi:10.1111/2041-210X.12826>. The package has functions to run MCMC
chains, plot results, evaluate convergence, and summarize posterior
distributions.

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
