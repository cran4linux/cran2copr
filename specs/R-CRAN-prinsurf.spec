%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prinsurf
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Constructs Principal Surfaces

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-rgl 

%description
Construct a principal surface that are two-dimensional surfaces that pass
through the middle of a p-dimensional data set. They minimise the distance
from the data points, and provide a nonlinear summary of data. The
surfaces are nonparametric and their shape is suggested by the data. The
formation of a surface is found using an iterative procedure which starts
with a linear summary, typically with a principal component plane. Each
successive iteration is a local average of the p-dimensional points, where
an average is based on a projection of a point onto the nonlinear surface
of the previous iteration. For more information on principal surfaces, see
Ganey, R. (2019,
"https://open.uct.ac.za/items/4e655d7d-d10c-481b-9ccc-801903aebfc8").

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
