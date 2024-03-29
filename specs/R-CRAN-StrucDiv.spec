%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StrucDiv
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Structural Diversity Quantification in Raster Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-raster >= 3.1.5
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-raster >= 3.1.5
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-glue 

%description
Spatial structural diversity refers to the spatial, i.e. horizontal
arrangement of landscape elements and can reveal itself as landscape
features, such as patches and linear features. The 'R' package 'StrucDiv'
provides methods to quantify spatial structural diversity in continuous
remote sensing data, or in other data in raster format. Structure is based
on the spatial arrangement of value pairs. The 'R' package 'StrucDiv'
includes methods to combine information from different spatial scales,
which allows to quantify multi-scale spatial structural diversity.

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
