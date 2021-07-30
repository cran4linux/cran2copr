%global __brp_check_rpaths %{nil}
%global packname  MALDIquant
%global packver   1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.20
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Analysis of Mass Spectrometry Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-parallel 

%description
A complete analysis pipeline for matrix-assisted laser
desorption/ionization-time-of-flight (MALDI-TOF) and other two-dimensional
mass spectrometry data. In addition to commonly used plotting and
processing methods it includes distinctive features, namely baseline
subtraction methods such as morphological filters (TopHat) or the
statistics-sensitive non-linear iterative peak-clipping algorithm (SNIP),
peak alignment using warping functions, handling of replicated
measurements as well as allowing spectra with different resolutions.

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
