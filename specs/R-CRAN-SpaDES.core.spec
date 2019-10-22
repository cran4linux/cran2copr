%global packname  SpaDES.core
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          Core Utilities for Developing and Running Spatially ExplicitDiscrete Event Simulation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-R.utils >= 2.5.0
BuildRequires:    R-CRAN-DEoptim >= 2.2.4
BuildRequires:    R-CRAN-lubridate >= 1.3.3
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-stringi >= 1.1.3
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-DiagrammeR >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-reproducible >= 0.2.10
BuildRequires:    R-CRAN-fpCompare >= 0.2.1
BuildRequires:    R-CRAN-quickPlot >= 0.1.4
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-codetools 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fastdigest 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-stats 
BuildRequires:    R-tcltk 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-R.utils >= 2.5.0
Requires:         R-CRAN-DEoptim >= 2.2.4
Requires:         R-CRAN-lubridate >= 1.3.3
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-stringi >= 1.1.3
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-DiagrammeR >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-reproducible >= 0.2.10
Requires:         R-CRAN-fpCompare >= 0.2.1
Requires:         R-CRAN-quickPlot >= 0.1.4
Requires:         R-CRAN-backports 
Requires:         R-codetools 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fastdigest 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-RCurl 
Requires:         R-stats 
Requires:         R-tcltk 
Requires:         R-tools 
Requires:         R-utils 

%description
Provide the core discrete event simulation (DES) framework for
implementing spatially explicit simulation models. The core DES components
facilitate modularity, and easily enable the user to include additional
functionality by running user-built simulation modules. Now includes
(experimental) conditional scheduling.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/sampleModules
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
