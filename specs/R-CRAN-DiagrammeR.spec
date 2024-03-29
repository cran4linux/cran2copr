%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiagrammeR
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Graph/Network Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1
BuildRequires:    R-CRAN-readr >= 2.1.1
BuildRequires:    R-CRAN-visNetwork >= 2.1.0
BuildRequires:    R-CRAN-glue >= 1.5.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-igraph >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-scales >= 1.1
BuildRequires:    R-CRAN-tidyr >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-htmltools >= 0.5.2
BuildRequires:    R-CRAN-viridisLite >= 0.4.2
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-tibble >= 3.1
Requires:         R-CRAN-readr >= 2.1.1
Requires:         R-CRAN-visNetwork >= 2.1.0
Requires:         R-CRAN-glue >= 1.5.0
Requires:         R-CRAN-htmlwidgets >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-igraph >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-scales >= 1.1
Requires:         R-CRAN-tidyr >= 1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-htmltools >= 0.5.2
Requires:         R-CRAN-viridisLite >= 0.4.2
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-cli 

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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
