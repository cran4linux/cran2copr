%global packname  ITNr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Analysis of the International Trade Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-network 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-GoodmanKruskal 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-blockmodeling 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-CRAN-comtradr 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-tnet 
BuildRequires:    R-CRAN-WDI 
BuildRequires:    R-CRAN-xergm.common 
BuildRequires:    R-CRAN-networkDynamic 
Requires:         R-CRAN-network 
Requires:         R-stats 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-GoodmanKruskal 
Requires:         R-graphics 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-blockmodeling 
Requires:         R-CRAN-igraph 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-intergraph 
Requires:         R-CRAN-comtradr 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-tnet 
Requires:         R-CRAN-WDI 
Requires:         R-CRAN-xergm.common 
Requires:         R-CRAN-networkDynamic 

%description
Functions to clean and process international trade data into an
international trade network (ITN) are provided. It then provides a set a
functions to undertake analysis and plots of the ITN (extract the
backbone, centrality, blockmodels, clustering). Examining the key players
in the ITN and regional trade patterns.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
