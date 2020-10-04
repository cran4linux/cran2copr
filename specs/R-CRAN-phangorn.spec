%global packname  phangorn
%global packver   2.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.5
Release:          3%{?dist}%{?buildtag}
Summary:          Phylogenetic Reconstruction and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-igraph >= 1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-igraph >= 1.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-quadprog 
Requires:         R-Matrix 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-magrittr 

%description
Package contains methods for estimation of phylogenetic trees and networks
using Maximum Likelihood, Maximum Parsimony, distance methods and Hadamard
conjugation. Allows to compare trees, models selection and offers
visualizations for trees and split networks.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/phangorn_sticker.png
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
