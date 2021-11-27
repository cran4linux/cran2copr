%global __brp_check_rpaths %{nil}
%global packname  eseis
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Environmental Seismology Toolbox

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-multitaper 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-IRISSeismic 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-EMMAgeo 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-minpack.lm 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-sp 
Requires:         R-CRAN-multitaper 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-fftw 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-IRISSeismic 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-EMMAgeo 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-minpack.lm 

%description
Environmental seismology is a scientific field that studies the seismic
signals, emitted by Earth surface processes. This package provides all
relevant functions to read/write seismic data files, prepare, analyse and
visualise seismic data, and generate reports of the processing history.

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
