%global packname  rmcfs
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          The MCFS-ID Algorithm for Feature Selection and InterdependencyDiscovery

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.70
Requires:         R-core >= 2.70
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.0.1
BuildRequires:    R-CRAN-rJava >= 0.5.0
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-data.table >= 1.0.1
Requires:         R-CRAN-rJava >= 0.5.0
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-igraph 

%description
MCFS-ID (Monte Carlo Feature Selection and Interdependency Discovery) is a
Monte Carlo method-based tool for feature selection. It also allows for
the discovery of interdependencies between the relevant features. MCFS-ID
is particularly suitable for the analysis of high-dimensional, 'small n
large p' transactional and biological data. M. Draminski, J. Koronacki
(2018) <doi:10.18637/jss.v085.i12>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cfg
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
