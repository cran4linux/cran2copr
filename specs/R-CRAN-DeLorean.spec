%global packname  DeLorean
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          3%{?dist}
Summary:          Estimates Pseudotimes for Single Cell Expression Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-reshape2 >= 1.4
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-stringr >= 0.6.2
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-functional 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-fastICA 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-memoise 
Requires:         R-MASS >= 7.3
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-reshape2 >= 1.4
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-stringr >= 0.6.2
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-methods 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-coda 
Requires:         R-parallel 
Requires:         R-CRAN-functional 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-fastICA 
Requires:         R-CRAN-seriation 
Requires:         R-lattice 
Requires:         R-CRAN-memoise 

%description
Implements the DeLorean model (Reid & Wernisch (2016)
<doi:10.1093/bioinformatics/btw372>) to estimate pseudotimes for single
cell expression data. The DeLorean model uses a Gaussian process latent
variable model to model uncertainty in the capture time of cross-sectional
data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/Rmd
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
