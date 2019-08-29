%global packname  emIRT
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}
Summary:          EM Algorithms for Estimating Item Response Theory Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-pscl >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-pscl >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.10.6

%description
Various Expectation-Maximization (EM) algorithms are implemented for item
response theory (IRT) models. The current implementation includes IRT
models for binary and ordinal responses, along with dynamic and
hierarchical IRT models with binary responses. The latter two models are
derived and implemented using variational EM.  Subsequent edits also
include variational network and text scaling models.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
