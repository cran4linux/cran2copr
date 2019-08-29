%global packname  loose.rock
%global packver   1.0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.16
Release:          1%{?dist}
Summary:          Tools for Survival Analysis and Data Science

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-futile.options 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-futile.options 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 

%description
Collection of functions to improve work-flow in survival analysis and data
science. The package features include: the generation of balanced
datasets, live retrieval of protein coding genes from two public
databases, generation of random matrix based on covariance matrix, cache
function to store function results. This work was supported by two grants
from the Portuguese Foundation for Science and technology, and the EU
Commission under SOUND project.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
