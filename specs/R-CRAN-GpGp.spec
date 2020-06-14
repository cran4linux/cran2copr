%global packname  GpGp
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Fast Gaussian Process Computation Using Vecchia's Approximation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-FNN 

%description
Functions for fitting and doing predictions with Gaussian process models
using Vecchia's (1988) approximation. Package also includes functions for
reordering input locations, finding ordered nearest neighbors (with help
from 'FNN' package), grouping operations, and conditional simulations.
Covariance functions for spatial and spatial-temporal data on Euclidean
domains and spheres are provided. The original approximation is due to
Vecchia (1988) <http://www.jstor.org/stable/2345768>, and the reordering
and grouping methods are from Guinness (2018)
<doi:10.1080/00401706.2018.1437476>. Model fitting employs a Fisher
scoring algorithm described in Guinness (2019) <arXiv:1905.08374>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
