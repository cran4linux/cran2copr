%global __brp_check_rpaths %{nil}
%global packname  spatstat.Knet
%global packver   2.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extension to 'spatstat' for Large Datasets on a Linear Network

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.core >= 2.3.2
BuildRequires:    R-CRAN-spatstat.linnet >= 2.3.1
BuildRequires:    R-CRAN-spatstat.utils >= 2.1
BuildRequires:    R-CRAN-spatstat.data >= 2.0
BuildRequires:    R-CRAN-spatstat.sparse >= 2.0
BuildRequires:    R-CRAN-spatstat.geom >= 2.0
BuildRequires:    R-CRAN-spatstat.random >= 2.0
BuildRequires:    R-CRAN-spatstat >= 2.0
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-spatstat.core >= 2.3.2
Requires:         R-CRAN-spatstat.linnet >= 2.3.1
Requires:         R-CRAN-spatstat.utils >= 2.1
Requires:         R-CRAN-spatstat.data >= 2.0
Requires:         R-CRAN-spatstat.sparse >= 2.0
Requires:         R-CRAN-spatstat.geom >= 2.0
Requires:         R-CRAN-spatstat.random >= 2.0
Requires:         R-CRAN-spatstat >= 2.0
Requires:         R-CRAN-Matrix 

%description
Extension to the 'spatstat' family of packages, for analysing large
datasets of spatial points on a network. The geometrically- corrected K
function is computed using a memory-efficient tree-based algorithm
described by Rakshit, Baddeley and Nair (2019).

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
