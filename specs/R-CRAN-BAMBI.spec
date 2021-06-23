%global __brp_check_rpaths %{nil}
%global packname  BAMBI
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bivariate Angular Mixture Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-loo >= 2.1.0
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-qrng 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-label.switching 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-loo >= 2.1.0
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-graphics 
Requires:         R-lattice 
Requires:         R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-tcltk 
Requires:         R-CRAN-qrng 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-gtools 
Requires:         R-parallel 
Requires:         R-CRAN-label.switching 
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-numDeriv 

%description
Fit (using Bayesian methods) and simulate mixtures of univariate and
bivariate angular distributions. Chakraborty and Wong (2017)
<arXiv:1708.07804>.

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
