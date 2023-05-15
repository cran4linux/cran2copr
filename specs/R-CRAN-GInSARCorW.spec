%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GInSARCorW
%global packver   1.15.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15.8
Release:          1%{?dist}%{?buildtag}
Summary:          GACOS InSAR Correction Workflow

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-sp 

%description
A workflow for correction of Differential Interferometric Synthetic
Aperture Radar (DInSAR) atmospheric delay base on Generic Atmospheric
Correction Online Service for InSAR (GACOS) data and correction algorithms
proposed by Chen Yu. This package calculate the Both Zenith and LOS
direction (User Depend). You have to just download GACOS product on your
area and preprocessed D-InSAR unwrapped images. Cite those references and
this package in your work, when using this framework. References: Yu, C.,
N. T. Penna, and Z. Li (2017) <doi:10.1016/j.rse.2017.10.038>. Yu, C., Li,
Z., & Penna, N. T. (2017) <doi:10.1016/j.rse.2017.10.038>. Yu, C., Penna,
N. T., and Li, Z. (2017) <doi:10.1002/2016JD025753>.

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
