%global packname  mvMORPH
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Multivariate Comparative Tools for Fitting Evolutionary Modelsto Morphometric Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.1
Requires:         R-core >= 2.9.1
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-glassoFast 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-subplex 
Requires:         R-stats 
Requires:         R-CRAN-spam 
Requires:         R-graphics 
Requires:         R-CRAN-glassoFast 

%description
Fits multivariate (Brownian Motion, Early Burst, ACDC, Ornstein-Uhlenbeck
and Shifts) models of continuous traits evolution on trees and time
series. 'mvMORPH' also proposes high-dimensional multivariate comparative
tools (linear models using Generalized Least Squares) based on penalized
likelihood.  See Clavel et al. (2015) <DOI:10.1111/2041-210X.12420> and
Clavel et al. (2018) <DOI:10.1093/sysbio/syy045>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
