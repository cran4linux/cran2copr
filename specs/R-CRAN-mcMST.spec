%global __brp_check_rpaths %{nil}
%global packname  mcMST
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Toolbox for the Multi-Criteria Minimum Spanning Tree Problem

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ecr >= 2.1.0
BuildRequires:    R-CRAN-BBmisc >= 1.6
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-parallelMap >= 1.3
BuildRequires:    R-CRAN-checkmate >= 1.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-lhs 
Requires:         R-CRAN-ecr >= 2.1.0
Requires:         R-CRAN-BBmisc >= 1.6
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-parallelMap >= 1.3
Requires:         R-CRAN-checkmate >= 1.1
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-lhs 

%description
Algorithms to approximate the Pareto-front of multi-criteria minimum
spanning tree problems. Additionally, a modular toolbox for the generation
of multi-objective benchmark graph problems is included.

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
