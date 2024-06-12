%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SoilSaltIndex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Soil Salinity Indices Generation using Satellite Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 

%description
The developed function generates soil salinity indices using satellite
data, utilizing multiple spectral bands such as Blue, Green, Red,
Near-Infrared (NIR), and Shortwave Infrared (SWIR1, SWIR2). It computes 24
different salinity indices crucial for monitoring and analyzing
salt-affected soils efficiently. For more details see, Rani, et al.
(2022). <DOI: 10.1007/s12517-022-09682-3>. One of the key features of the
developed function is its flexibility. Users can provide any combination
of the required spectral bands, and the function will automatically
calculate only the relevant indices based on the available data. This
dynamic capability ensures that users can maximize the utility of their
data without the need for all spectral bands, making the package versatile
and user-friendly. Outputs are provided as GeoTIFF file format,
facilitating easy integration with GIS workflows.

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
