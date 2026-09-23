%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sptrends
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference for Spatiotemporal Trends in Gridded Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.2.0
BuildRequires:    R-CRAN-terra >= 1.7.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-withr >= 2.2.0
Requires:         R-CRAN-terra >= 1.7.0
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Provides a unified and reproducible framework for statistical inference of
spatiotemporal trends in gridded environmental data. The framework
addresses the interconnected challenges of serial correlation, spatial
dependence and multiple testing that commonly arise when analysing gridded
environmental time series. Its core methods support serial-correlation
treatment through trend-preserving prewhitening, pixel-wise and spatially
explicit trend inference, slope estimation and multiple-testing
correction. These methods may be applied independently or integrated
within configurable analytical workflows. Dedicated workflows are also
provided to reproduce methodologies published in the scientific
literature: Gutiérrez-Hernández and García (2025)
<doi:10.1016/j.rsase.2024.101377> for the True Significant Trends
workflow, Gutiérrez-Hernández and García (2024) <doi:10.3390/rs16203886>
for the Robust Trend Analysis workflow, and Gutiérrez-Hernández and García
(2025) <doi:10.3390/math13223630> for the adaptive false discovery rate
procedure. Supporting utilities facilitate raster data import and
inspection, anomaly calculation, spatial autocorrelation diagnostics,
simulation studies, benchmarking, visualisation, mapping, and reporting.

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
