%global packname  linkcomm
%global packver   1.0-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Generating, Visualizing, and Analysing Link Communities in Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dynamicTreeCut 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dynamicTreeCut 
Requires:         R-grid 
Requires:         R-utils 

%description
Link communities reveal the nested and overlapping structure in networks,
and uncover the key nodes that form connections to multiple communities.
linkcomm provides a set of tools for generating, visualizing, and
analysing link communities in networks of arbitrary size and type. The
linkcomm package also includes tools for generating, visualizing, and
analysing Overlapping Cluster Generator (OCG) communities. Kalinka and
Tomancak (2011) <10.1093/bioinformatics/btr311>.

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
