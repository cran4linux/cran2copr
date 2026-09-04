%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  graphvec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vectorised Graph Data Structures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tibble 

%description
Extends vectors to include graph relationships between their elements, and
offers tools to compute useful summaries of the graph structure for use in
summarising, filtering, and otherwise manipulating the graph. Node
identity is positional rather than value-based, so isolated nodes and
repeated values are represented without special handling. Three
complementary data structures are provided, each an ordinary vector that
stays a column in a data frame and slices consistently with it: 'node_vec'
is vectorised along the nodes of a graph, 'edge_vec' is vectorised along
its edges, and 'agg_vec' (with the tabular 'agg_df') represents the
aggregation structure common in data analysis, such as a total row over a
set of categories. This makes graph relationships a native part of tidy
rectangular data analysis workflows, alongside tools such as those in
'dplyr'. Each of these can also be converted to 'igraph' objects for
further analysis.

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
