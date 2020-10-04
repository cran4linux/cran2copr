%global packname  BayesFactor
%global packver   0.9.12-4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.12.4.2
Release:          3%{?dist}%{?buildtag}
Summary:          Computation of Bayes Factors for Common Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-Matrix >= 1.1.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-MatrixModels 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-hypergeo 
Requires:         R-Matrix >= 1.1.1
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-coda 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-MatrixModels 
Requires:         R-methods 
Requires:         R-CRAN-hypergeo 

%description
A suite of functions for computing various Bayes factors for simple
designs, including contingency tables, one- and two-sample designs,
one-way designs, general ANOVA designs, and linear regression.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
