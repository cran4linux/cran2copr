%global packname  phylobase
%global packver   0.8.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.10
Release:          3%{?dist}%{?buildtag}
Summary:          Base Package for Phylogenetic Structures and Comparative Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape >= 3.0
BuildRequires:    R-CRAN-rncl >= 0.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RNeXML 
Requires:         R-CRAN-ape >= 3.0
Requires:         R-CRAN-rncl >= 0.6.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-ade4 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-RNeXML 

%description
Provides a base S4 class for comparative methods, incorporating one or
more trees and trait data.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/nexmlfiles
%doc %{rlibdir}/%{packname}/nexusfiles
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
