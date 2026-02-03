%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BioGSP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Biological Graph Signal Processing for Spatial Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-viridis 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 

%description
Implementation of Graph Signal Processing (GSP) methods including Spectral
Graph Wavelet Transform (SGWT) for analyzing spatial patterns in
biological data. Based on Hammond, Vandergheynst, and Gribonval (2011)
<doi:10.1016/j.acha.2010.04.005>. Provides tools for multi-scale analysis
of biology spatial signals, including forward and inverse transforms,
energy analysis, and visualization functions tailored for biological
applications. Biological application example is on Stephanie, Yao, Yuzhou
(2024) <doi:10.1101/2024.12.20.629650>.

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
