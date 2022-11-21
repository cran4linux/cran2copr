%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DRHotNet
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Differential Risk Hotspots in a Linear Network

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-PBSmapping 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.linnet 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-PBSmapping 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.linnet 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-utils 

%description
Performs the identification of differential risk hotspots (Briz-Redon et
al. 2019) <doi:10.1016/j.aap.2019.105278> along a linear network. Given a
marked point pattern lying on the linear network, the method implemented
uses a network-constrained version of kernel density estimation (McSwiggan
et al. 2017) <doi:10.1111/sjos.12255> to approximate the probability of
occurrence across space for the type of event specified by the user
through the marks of the pattern (Kelsall and Diggle 1995)
<doi:10.2307/3318678>. The goal is to detect microzones of the linear
network where the type of event indicated by the user is overrepresented.

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
