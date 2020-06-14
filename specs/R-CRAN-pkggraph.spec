%global packname  pkggraph
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          A Consistent and Intuitive Platform to Explore the Dependenciesof Packages on the Comprehensive R Archive Network LikeRepositories

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.5
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-intergraph >= 2.0.2
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-tibble >= 1.3.0
BuildRequires:    R-Matrix >= 1.2.10
BuildRequires:    R-CRAN-network >= 1.13
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-ggnetwork >= 0.5.1
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-networkD3 >= 0.4
BuildRequires:    R-CRAN-htmltools >= 0.3.5
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 2.5
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-intergraph >= 2.0.2
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-tibble >= 1.3.0
Requires:         R-Matrix >= 1.2.10
Requires:         R-CRAN-network >= 1.13
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-ggnetwork >= 0.5.1
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-networkD3 >= 0.4
Requires:         R-CRAN-htmltools >= 0.3.5
Requires:         R-tools 
Requires:         R-utils 

%description
Interactively explore various dependencies of a package(s) (on the
Comprehensive R Archive Network Like repositories) and perform analysis
using tidy philosophy. Most of the functions return a 'tibble' object
(enhancement of 'dataframe') which can be used for further analysis. The
package offers functions to produce 'network' and 'igraph' dependency
graphs. The 'plot' method produces a static plot based on 'ggnetwork' and
'plotd3' function produces an interactive D3 plot based on 'networkD3'.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
