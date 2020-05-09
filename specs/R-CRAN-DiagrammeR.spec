%global packname  DiagrammeR
%global packver   1.0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6.1
Release:          1%{?dist}
Summary:          Graph/Network Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-visNetwork >= 2.0.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-igraph >= 1.2.2
BuildRequires:    R-CRAN-htmlwidgets >= 1.2
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-downloader >= 0.4
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rlang >= 0.2.2
BuildRequires:    R-CRAN-influenceR >= 0.1.0
Requires:         R-CRAN-visNetwork >= 2.0.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-htmlwidgets >= 1.2
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-downloader >= 0.4
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-influenceR >= 0.1.0

%description
Build graph/network structures using functions for stepwise addition and
deletion of nodes and edges. Work with data available in tables for bulk
addition of nodes, edges, and associated metadata. Use graph selections
and traversals to apply changes to specific nodes or edges. A wide
selection of graph algorithms allow for the analysis of graphs. Visualize
the graphs and take advantage of any aesthetic properties assigned to
nodes and edges.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
