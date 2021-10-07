%global __brp_check_rpaths %{nil}
%global packname  spherepc
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Spherical Principal Curves

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-sphereplot 
BuildRequires:    R-stats 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-sphereplot 
Requires:         R-stats 

%description
Fitting dimension reduction methods to data lying on two-dimensional
sphere. This package provides principal circle, principal geodesic
analysis, Hauberg's principal curves, and spherical principal curves.
Moreover, it offers the method of locally defined principal geodesics
which is underway.The detailed procedures are described in Lee, J., Kim,
J.-H. and Oh, H.-S. (2021) <doi:10.1109/TPAMI.2020.3025327>. Also see Kim,
J.-H., Lee, J. and Oh, H.-S. (2020) <arXiv:2003.02578>.

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
