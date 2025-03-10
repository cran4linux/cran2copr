%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  raybevel
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generates Polygon Straight Skeletons and 3D Bevels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppCGAL >= 6.0.1
BuildRequires:    R-CRAN-RcppThread >= 2.1.6
BuildRequires:    R-CRAN-rayvertex >= 0.11.4
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-decido 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-rayvertex >= 0.11.4
Requires:         R-CRAN-progress 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-decido 
Requires:         R-CRAN-sf 
Requires:         R-grid 

%description
Generates polygon straight skeletons and 3D models. Provides functions to
create and visualize interior polygon offsets, 3D beveled polygons, and 3D
roof models.

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
