%global packname  OpenMx
%global packver   2.17.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.17.3
Release:          1%{?dist}
Summary:          Extended Structural Equation Modelling

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-StanHeaders >= 2.10.0.2
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-rpf >= 0.45
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-digest 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 

%description
Create structural equation models that can be manipulated
programmatically. Models may be specified with matrices or paths (LISREL
or RAM) Example models include confirmatory factor, multiple group,
mixture distribution, categorical threshold, modern test theory,
differential Fit functions include full information maximum likelihood,
maximum likelihood, and weighted least squares. equations, state space,
and many others. Support and advanced package binaries available at
<http://openmx.ssri.psu.edu>. The software is described in Neale, Hunter,
Pritikin, Zahery, Brick, Kirkpatrick, Estabrook, Bates, Maes, & Boker
(2016) <doi:10.1007/s11336-014-9435-8>.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;
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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/models
%doc %{rlibdir}/%{packname}/mx-scripts
%doc %{rlibdir}/%{packname}/no-npsol
%doc %{rlibdir}/%{packname}/tools
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
