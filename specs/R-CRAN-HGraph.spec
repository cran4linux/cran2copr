%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HGraph
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Use Graph Structure to Travel

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-CRAN-knitr 

%description
It is used to travel graphs, by using DFS and BFS to get the path from
node to each leaf node. Depth first traversal(DFS) is a recursive
algorithm for searching all the vertices of a graph or tree data
structure. Traversal means visiting all the nodes of a graph. Breadth
first traversal(BFS) algorithm is used to search a tree or graph data
structure for a node that meets a set of criteria. It starts at the tree’s
root or graph and searches/visits all nodes at the current depth level
before moving on to the nodes at the next depth level. Also, it provides
the matrix which is reachable between each node. Implement reference about
Baruch Awerbuch (1985) <doi:10.1016/0020-0190(85)90083-3>.

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
