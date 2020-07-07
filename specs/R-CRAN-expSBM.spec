%global packname  expSBM
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          3%{?dist}
Summary:          An Exponential Stochastic Block Model for Interaction Lengths

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-blockmodels 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-blockmodels 

%description
Given a continuous-time dynamic network, this package allows one to fit a
stochastic blockmodel where nodes belonging to the same group create
interactions and non-interactions of similar lengths. This package
implements the methodology described by R. Rastelli and M. Fop (2019)
<arXiv:1901.09828>.

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
