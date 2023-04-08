%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pgirmess
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Analysis and Data Mining for Field Ecologists

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-boot >= 1.3.4
BuildRequires:    R-CRAN-spdep >= 1.1.7
BuildRequires:    R-CRAN-sf >= 1.0.4
BuildRequires:    R-CRAN-sp >= 0.9.97
Requires:         R-CRAN-boot >= 1.3.4
Requires:         R-CRAN-spdep >= 1.1.7
Requires:         R-CRAN-sf >= 1.0.4
Requires:         R-CRAN-sp >= 0.9.97

%description
Set of tools for reading, writing and transforming spatial and seasonal
data, model selection and specific statistical tests for ecologists. It
includes functions to interpolate regular positions of points between
landmarks, to discretize polylines into regular point positions, link
distant observations to points and convert a bounding box in a spatial
object. It also provides miscellaneous functions for field ecologists such
as spatial statistics and inference on diversity indexes, writing
data.frame with Chinese characters.

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
