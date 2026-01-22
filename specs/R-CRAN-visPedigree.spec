%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visPedigree
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tidying and Visualizing Animal Pedigrees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nadiv >= 2.18.0
BuildRequires:    R-CRAN-igraph >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-nadiv >= 2.18.0
Requires:         R-CRAN-igraph >= 1.3.0
Requires:         R-CRAN-data.table >= 1.14.0

%description
Built on graph theory and the high-performance 'data.table' framework,
this package provides a comprehensive suite of tools for tidying, pruning,
and visualizing animal pedigrees. By modeling pedigrees as directed
acyclic graphs using 'igraph', it ensures robust loop detection, efficient
generation assignment, and sophisticated hierarchical layouts. Key
features include standardizing pedigree formats, flexible ancestry
tracing, and generating legible vector-based PDF graphs. A unique
compaction algorithm enables the visualization of massive pedigrees (e.g.,
in aquaculture selective breeding population) by grouping full-sib
families, maintaining structural clarity without overcrowding.

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
