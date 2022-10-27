%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  espadon
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Study of Patient DICOM Data in Oncology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-rgl >= 0.107.14
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-js 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-qs 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-rgl >= 0.107.14
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-DT 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-js 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-misc3d 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-qs 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
Exploitation, processing and 2D-3D visualization of DICOM-RT files
(structures, dosimetry, imagery) for medical physics and clinical
research, in a patient-oriented perspective.

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
