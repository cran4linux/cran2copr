%global packname  pems.utils
%global packver   0.2.26.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.26.4
Release:          3%{?dist}
Summary:          Portable Emissions (and Other Mobile) Measurement SystemUtilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-loa 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-baseline 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-lattice 
Requires:         R-CRAN-loa 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-baseline 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 

%description
Utility functions for the handling, analysis and visualisation of data
from portable emissions measurement systems ('PEMS') and other similar
mobile activity monitoring devices. The package includes a dedicated
'pems' data class that manages many of the quality control, unit handling
and data archiving issues that can hinder efforts to standardise 'PEMS'
research.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
