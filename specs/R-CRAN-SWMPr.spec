%global packname  SWMPr
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          2%{?dist}
Summary:          Retrieving, Organizing, and Analyzing Estuary Monitoring Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-oce 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-oce 
Requires:         R-CRAN-dplyr 
Requires:         R-lattice 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-XML 

%description
Tools for retrieving, organizing, and analyzing environmental data from
the System Wide Monitoring Program of the National Estuarine Research
Reserve System <http://cdmo.baruch.sc.edu/>. These tools address common
challenges associated with continuous time series data for environmental
decision making.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/stat_locs.csv
%{rlibdir}/%{packname}/INDEX
