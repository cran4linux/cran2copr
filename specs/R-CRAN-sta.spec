%global __brp_check_rpaths %{nil}
%global packname  sta
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Seasonal Trend Analysis for Time Series Imagery in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.6.1
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-CRAN-mapview >= 2.7.0
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-trend >= 1.1.1
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-iterators >= 1.0.10
BuildRequires:    R-CRAN-rgdal >= 0.9.1
BuildRequires:    R-CRAN-geoTS >= 0.1.1
BuildRequires:    R-methods 
Requires:         R-parallel >= 3.6.1
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-CRAN-mapview >= 2.7.0
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-trend >= 1.1.1
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-iterators >= 1.0.10
Requires:         R-CRAN-rgdal >= 0.9.1
Requires:         R-CRAN-geoTS >= 0.1.1
Requires:         R-methods 

%description
Efficiently estimate shape parameters of periodic time series imagery
(raster stacks) with which a statistical seasonal trend analysis (STA) is
subsequently performed. STA output can be exported in conventional raster
formats. Methods to visualize STA output are also implemented as well as
the calculation of additional basic statistics. STA is based on (R.
Eastman, F. Sangermano, B. Ghimire, H. Zhu, H. Chen, N. Neeti, Y. Cai, E.
Machado and S. Crema, 2009) <doi:10.1080/01431160902755338>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
