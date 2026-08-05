%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MALDIassist
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mathematical Utilities for MALDI-TOF Mass Spectrometry

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gtools 

%description
Supports matrix-assisted laser desorption/ionization time-of-flight
(MALDI-TOF) mass spectrometry workflows from raw Bruker spectra to
cohort-level peak matrices. Provides spectrum loading, Savitzky-Golay
smoothing, baseline correction (SNIP and TopHat), Gaussian
kernel-regression-based peak detection including shoulder peaks,
peak-quality assessment, filtering, and cohort feature analysis.
Computationally intensive routines are implemented in C++ using 'Rcpp'.
The implemented signal-processing methods include those described by
Savitzky and Golay (1964) <doi:10.1021/ac60214a047>, Ryan et al. (1988)
<doi:10.1016/0168-583X(88)90063-8>, Stanford, Bagley and Solomon (2016)
<doi:10.1186/s12953-016-0107-8>, and Nadaraya-Watson kernel regression
(Nadaraya (1964) <doi:10.1137/1109020>; Watson (1964)
<https://www.jstor.org/stable/25049340>).

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
