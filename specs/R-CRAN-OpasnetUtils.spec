%global __brp_check_rpaths %{nil}
%global packname  OpasnetUtils
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Opasnet Modelling Environment Utility Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-httpRequest 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-igraph 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-httpRequest 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-igraph 

%description
Contains tools for open assessment and modelling in Opasnet, a wiki-based
web site and workspace for societal decision making (see
<http://en.opasnet.org/w/Main_Page> for more information). The core
principle of the workspace is maximal openness and modularity. Variables
are defined on public wiki pages using wiki inputs/tables, databases and R
code. This package provides the functionality to download and use these
variables. It also contains health impact assessment tools such as spatial
methods for exposure modelling.

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
%{rlibdir}/%{packname}/INDEX
