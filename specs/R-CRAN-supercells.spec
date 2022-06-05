%global __brp_check_rpaths %{nil}
%global packname  supercells
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Superpixels of Spatial Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-terra >= 1.4.21
BuildRequires:    R-CRAN-philentropy >= 0.6.0
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-terra >= 1.4.21
Requires:         R-CRAN-philentropy >= 0.6.0
Requires:         R-CRAN-sf 
Requires:         R-CRAN-future.apply 

%description
Creates superpixels based on input spatial data. This package works on
spatial data with one variable (e.g., continuous raster), many variables
(e.g., RGB rasters), and spatial patterns (e.g., areas in categorical
rasters). It is based on the SLIC algorithm (Achanta et al. (2012)
<doi:10.1109/TPAMI.2012.120>), and readapts it to work with arbitrary
dissimilarity measures.

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
