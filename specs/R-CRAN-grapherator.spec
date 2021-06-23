%global __brp_check_rpaths %{nil}
%global packname  grapherator
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Modular Multi-Step Graph Generator

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BBmisc >= 1.6
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-checkmate >= 1.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-BBmisc >= 1.6
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-checkmate >= 1.1
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-deldir 
Requires:         R-grDevices 

%description
Set of functions for step-wise generation of (weighted) graphs. Aimed for
research in the field of single- and multi-objective combinatorial
optimization. Graphs are generated adding nodes, edges and weights. Each
step may be repeated multiple times with different predefined and custom
generators resulting in high flexibility regarding the graph topology and
structure of edge weights.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
