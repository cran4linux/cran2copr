%global packname  pacotest
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Testing for Partial Copulas and the Simplifying Assumption inVine Copulas

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-VineCopula >= 2.0.5
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-VineCopula >= 2.0.5
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 

%description
Routines for two different test types, the Constant Conditional
Correlation (CCC) test and the Vectorial Independence (VI) test are
provided (Kurz and Spanhel (2017) <arXiv:1706.02338>). The tests can be
applied to check whether a conditional copula coincides with its partial
copula. Functions to test whether a regular vine copula satisfies the
so-called simplifying assumption or to test a single copula within a
regular vine copula to be a (j-1)-th order partial copula are available.
The CCC test comes with a decision tree approach to allow testing in
high-dimensional settings.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
