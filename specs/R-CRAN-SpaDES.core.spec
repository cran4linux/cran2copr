%global packname  SpaDES.core
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Core Utilities for Developing and Running Spatially ExplicitDiscrete Event Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-R.utils >= 2.5.0
BuildRequires:    R-CRAN-lubridate >= 1.3.3
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-stringi >= 1.1.3
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-reproducible >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-qs >= 0.21.1
BuildRequires:    R-CRAN-fpCompare >= 0.2.1
BuildRequires:    R-CRAN-quickPlot >= 0.1.4
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fastdigest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-tcltk 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-R.utils >= 2.5.0
Requires:         R-CRAN-lubridate >= 1.3.3
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-stringi >= 1.1.3
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-reproducible >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-qs >= 0.21.1
Requires:         R-CRAN-fpCompare >= 0.2.1
Requires:         R-CRAN-quickPlot >= 0.1.4
Requires:         R-CRAN-backports 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fastdigest 
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-tcltk 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-whisker 

%description
Provides the core framework for a discrete event system (DES) to implement
a complete data-to-decisions, reproducible workflow. The core DES
components facilitate modularity, and easily enable the user to include
additional functionality by running user-built modules. Includes
conditional scheduling, restart after interruption, packaging of reusable
modules, tools for developing arbitrary automated workflows, automated
interweaving of modules of different temporal resolution, and tools for
visualizing and understanding the DES project.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/sampleModules
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
