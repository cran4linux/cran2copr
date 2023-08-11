%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SOAs
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Creation of Stratum Orthogonal Arrays

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DoE.base >= 1.2
BuildRequires:    R-CRAN-lhs >= 1.1.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-FrF2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-conf.design 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-partitions 
Requires:         R-CRAN-DoE.base >= 1.2
Requires:         R-CRAN-lhs >= 1.1.3
Requires:         R-stats 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-FrF2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-conf.design 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-partitions 

%description
Creates stratum orthogonal arrays (also known as strong orthogonal
arrays). These are arrays with more levels per column than the typical
orthogonal array, and whose low order projections behave like orthogonal
arrays, when collapsing levels to coarser strata. Details are described in
Groemping (2022) "A unifying implementation of stratum (aka strong)
orthogonal arrays"
<http://www1.bht-berlin.de/FB_II/reports/Report-2022-002.pdf>.

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
