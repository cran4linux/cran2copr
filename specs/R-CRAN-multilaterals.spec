%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multilaterals
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transitive Index Numbers for Cross-Sections and Panel Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-igraph 

%description
Computing transitive (and non-transitive) index numbers (Coelli et al.,
2005 <doi:10.1007/b136381>) for cross-sections and panel data. For the
calculation of transitive indexes, the EKS (Coelli et al., 2005
<doi:10.1007/b136381>; Rao et al., 2002 <doi:10.1007/978-1-4615-0851-9_4>)
and Minimum spanning tree (Hill, 2004 <doi:10.1257/0002828043052178>)
methods are implemented. Traditional fixed-base and chained indexes, and
their growth rates, can also be derived using the Paasche, Laspeyres,
Fisher and Tornqvist formulas.

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
