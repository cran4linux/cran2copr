%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rlibkdv
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Versatile Kernel Density Visualization Library for Geospatial Analytics (Heatmap)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sf 

%description
Unlock the power of large-scale geospatial analysis, quickly generate
high-resolution kernel density visualizations, supporting advanced
analysis tasks such as bandwidth-tuning and spatiotemporal analysis.
Regardless of the size of your dataset, our library delivers efficient and
accurate results. Tsz Nam Chan, Leong Hou U, Byron Choi, Jianliang Xu,
Reynold Cheng (2023) <doi:10.1145/3555041.3589401>. Tsz Nam Chan, Rui
Zang, Pak Lon Ip, Leong Hou U, Jianliang Xu (2023)
<doi:10.1145/3555041.3589711>. Tsz Nam Chan, Leong Hou U, Byron Choi,
Jianliang Xu (2022) <doi:10.1145/3514221.3517823>. Tsz Nam Chan, Pak Lon
Ip, Kaiyan Zhao, Leong Hou U, Byron Choi, Jianliang Xu (2022)
<doi:10.14778/3554821.3554855>. Tsz Nam Chan, Pak Lon Ip, Leong Hou U,
Byron Choi, Jianliang Xu (2022) <doi:10.14778/3503585.3503591>. Tsz Nam
Chan, Pak Lon Ip, Leong Hou U, Byron Choi, Jianliang Xu (2022)
<doi:10.14778/3494124.3494135>. Tsz Nam Chan, Pak Lon Ip, Leong Hou U,
Weng Hou Tong, Shivansh Mittal, Ye Li, Reynold Cheng (2021)
<doi:10.14778/3476311.3476312>. Tsz Nam Chan, Zhe Li, Leong Hou U,
Jianliang Xu, Reynold Cheng (2021) <doi:10.14778/3461535.3461540>. Tsz Nam
Chan, Reynold Cheng, Man Lung Yiu (2020) <doi:10.1145/3318464.3380561>.
Tsz Nam Chan, Leong Hou U, Reynold Cheng, Man Lung Yiu, Shivansh Mittal
(2020) <doi:10.1109/TKDE.2020.3018376>. Tsz Nam Chan, Man Lung Yiu, Leong
Hou U (2019) <doi:10.1109/ICDE.2019.00055>.

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
