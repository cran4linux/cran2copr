%global __brp_check_rpaths %{nil}
%global packname  edina
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of an Exploratory Deterministic Input, Noisyand Gate Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jjb 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rgen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jjb 
Requires:         R-CRAN-reshape2 

%description
Perform a Bayesian estimation of the exploratory deterministic input,
noisy and gate (EDINA) cognitive diagnostic model described by Chen et al.
(2018) <doi:10.1007/s11336-017-9579-4>.

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
%{rlibdir}/%{packname}
