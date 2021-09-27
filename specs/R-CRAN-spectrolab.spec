%global __brp_check_rpaths %{nil}
%global packname  spectrolab
%global packver   0.0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.16
Release:          1%{?dist}%{?buildtag}
Summary:          Class and Methods for Spectral Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-shinyjs >= 1.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.0
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-shinyjs >= 1.1
Requires:         R-CRAN-RColorBrewer >= 1.0
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-parallel 

%description
Input/Output, processing and visualization of spectra taken with different
spectrometers, including SVC (Spectra Vista), ASD and PSR (Spectral
Evolution). Implements an S3 class 'spectra' that other packages can build
on. Provides methods to access, plot, manipulate, splice sensor overlap,
vector normalize and smooth spectra.

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
