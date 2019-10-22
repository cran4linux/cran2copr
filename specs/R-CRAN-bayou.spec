%global packname  bayou
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Bayesian Fitting of Ornstein-Uhlenbeck Models to Phylogenies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-ape >= 3.0.6
BuildRequires:    R-CRAN-geiger >= 2.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-denstrip 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape >= 3.0.6
Requires:         R-CRAN-geiger >= 2.0
Requires:         R-CRAN-Rcpp >= 0.10.3
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-coda 
Requires:         R-MASS 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-denstrip 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-foreach 
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Tools for fitting and simulating multi-optima Ornstein-Uhlenbeck models to
phylogenetic comparative data using Bayesian reversible-jump methods.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
