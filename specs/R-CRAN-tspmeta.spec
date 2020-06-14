%global packname  tspmeta
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Instance Feature Calculation and Evolutionary InstanceGeneration for the Traveling Salesman Problem

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-checkmate >= 1.5
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-splancs 
Requires:         R-CRAN-checkmate >= 1.5
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-TSP 
Requires:         R-MASS 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-splancs 

%description
Instance feature calculation and evolutionary instance generation for the
traveling salesman problem. Also contains code to "morph" two TSP
instances into each other. And the possibility to conveniently run a
couple of solvers on TSP instances.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
