%global __brp_check_rpaths %{nil}
%global packname  TCIU
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spacekime Analytics, Time Complexity and Inferential Uncertainty

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-fancycut 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-AnalyzeFMRI 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-fmri 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-spatstat.core 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-MultiwayRegression 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-fancycut 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-AnalyzeFMRI 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-fmri 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-extraDistr 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-spatstat.core 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-MultiwayRegression 

%description
Provide the core functionality to transform longitudinal data to
complex-time (kime) data using analytic and numerical techniques,
visualize the original time-series and reconstructed kime-surfaces,
perform model based (e.g., tensor-linear regression) and model-free
classification and clustering methods in the book Dinov, ID and Velev, MV.
(2021) "Data Science: Time Complexity, Inferential Uncertainty, and
Spacekime Analytics", De Gruyter STEM Series, ISBN 978-3-11-069780-3.
<https://www.degruyter.com/view/title/576646>. The package includes 18
core functions which can be separated into three groups. 1) draw
longitudinal data, such as fMRI time-series, and forecast or transform the
time-series data. 2) simulate real-valued time-series data, e.g., fMRI
time-courses, detect the activated areas, report the corresponding
p-values, and visualize the p-values in the 3D brain space. 3) Laplace
transform and kimesurface reconstructions of the fMRI data.

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
