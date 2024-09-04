%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ravetools
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Signal and Image Processing Toolbox for Analyzing Intracranial Electroencephalography Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RNiftyReg >= 2.7.1
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-waveslim >= 1.8.2
BuildRequires:    R-CRAN-digest >= 0.6.29
BuildRequires:    R-CRAN-gsignal >= 0.3.5
BuildRequires:    R-CRAN-filearray >= 0.1.3
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-RNiftyReg >= 2.7.1
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-waveslim >= 1.8.2
Requires:         R-CRAN-digest >= 0.6.29
Requires:         R-CRAN-gsignal >= 0.3.5
Requires:         R-CRAN-filearray >= 0.1.3
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pracma 
Requires:         R-splines 

%description
Implemented fast and memory-efficient Notch-filter, Welch-periodogram,
discrete wavelet spectrogram for minutes of high-resolution signals, fast
3D convolution, image registration, 3D mesh manipulation; providing
fundamental toolbox for intracranial Electroencephalography (iEEG)
pipelines. Documentation and examples about 'RAVE' project are provided at
<https://openwetware.org/wiki/RAVE>, and the paper by John F. Magnotti,
Zhengjia Wang, Michael S. Beauchamp (2020)
<doi:10.1016/j.neuroimage.2020.117341>; see 'citation("ravetools")' for
details.

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
