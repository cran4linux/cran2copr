%global __brp_check_rpaths %{nil}
%global packname  HyperG
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hypergraphs in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-gtools 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements various tools for storing and analyzing hypergraphs. Handles
basic undirected, unweighted hypergraphs, and various ways of creating
hypergraphs from a number of representations, and converting between
graphs and hypergraphs.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
