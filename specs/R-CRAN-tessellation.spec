%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tessellation
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Delaunay and Voronoï Tessellations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-cxhull 
BuildRequires:    R-CRAN-english 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-utils 
Requires:         R-CRAN-cxhull 
Requires:         R-CRAN-english 
Requires:         R-graphics 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sets 
Requires:         R-utils 

%description
Delaunay and Voronoï tessellations, with emphasis on the two-dimensional
and the three-dimensional cases (the package provides functions to plot
the tessellations for these cases). Delaunay tessellations are computed in
C with the help of the 'Qhull' library <http://www.qhull.org/>.

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
