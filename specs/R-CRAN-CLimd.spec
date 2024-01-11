%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CLimd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generating Rainfall Rasters from IMD NetCDF Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-qpdf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-qpdf 

%description
The developed function is a comprehensive tool for the analysis of India
Meteorological Department (IMD) NetCDF rainfall data. Specifically
designed to process high-resolution daily gridded rainfall datasets. It
provides four key functions to process IMD NetCDF rainfall data and create
rasters for various temporal scales, including annual, seasonal, monthly,
and weekly rainfall. For method details see, Malik, A.
(2019).<DOI:10.1007/s12517-019-4454-5>. It supports different aggregation
methods, such as sum, min, max, mean, and standard deviation. These
functions are designed for spatio-temporal analysis of rainfall patterns,
trend analysis,geostatistical modeling of rainfall variability,
identifying rainfall anomalies and extreme events and can be an input for
hydrological and agricultural models.

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
