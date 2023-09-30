%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatialGraph
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          The SpatialGraph Class and Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-splancs 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-splancs 

%description
Provision of the S4 SpatialGraph class built on top of objects provided by
'igraph' and 'sp' packages, and associated utilities. See the
documentation of the SpatialGraph-class within this package for further
description. An example of how from a few points one can arrive to a
SpatialGraph is provided in the function sl2sg().

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
