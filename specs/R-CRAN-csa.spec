%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  csa
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Cross-Scale Analysis Tool for Model-Observation Visualization and Integration

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-Lmoments 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-Lmoments 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 

%description
Integration of Earth system data from various sources is a challenging
task. Except for their qualitative heterogeneity, different data records
exist for describing similar Earth system process at different
spatio-temporal scales. Data inter-comparison and validation are usually
performed at a single spatial or temporal scale, which could hamper the
identification of potential discrepancies in other scales. 'csa' package
offers a simple, yet efficient, graphical method for synthesizing and
comparing observed and modelled data across a range of spatio-temporal
scales. Instead of focusing at specific scales, such as annual means or
original grid resolution, we examine how their statistical properties
change across spatio-temporal continuum.

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
