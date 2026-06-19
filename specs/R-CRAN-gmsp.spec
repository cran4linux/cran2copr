%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gmsp
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Ground Motion Signal Processing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-EMD 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-hht 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-spectral 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VMDecomp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-EMD 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-hht 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-spectral 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-VMDecomp 

%description
Implements short-time Fourier transform (STFT) based processing of
strong-motion time series: time-grid regularisation, STFT-window and
anti-alias-resampling strategy selection, edge tapering, and
frequency-domain integration and differentiation, mapping a single input
(acceleration, velocity, or displacement) to a consistent triplet under a
chosen analysis bandwidth. Also provides intrinsic-mode-function
decomposition via empirical mode decomposition (EMD), ensemble EMD (EEMD),
and variational mode decomposition (VMD) with optional band-rule
filtering; elastic single-degree-of-freedom (SDOF) response spectra
(pseudo-spectral acceleration, velocity, and displacement) by exact
state-space integration; intensity measures including peak,
root-mean-square (RMS), Arias intensity, significant-duration, cumulative
absolute velocity, mean period, and the derived indices earthquake
destructiveness potential (EPI) and power-of-input (PDI); and D50 and D100
horizontal response spectra. Methods: Huang et al. (1998)
<doi:10.1098/rspa.1998.0193>, Wu and Huang (2009)
<doi:10.1142/S1793536909000047>, Dragomiretskiy and Zosso (2014)
<doi:10.1109/TSP.2013.2288675>, Boore (2010) <doi:10.1785/0120090179>. An
optional indexing layer parses provider files in formats including 'PEER'
'NGA-West2' 'AT2', 'CESMD' 'V2'/'V2c', 'NWZ' 'V2A', Geological Survey of
Canada 'TR', 'IGP'/'UCR' 'AC' variants, and generic two-column ASCII text,
normalises components, writes per-record CSV (comma-separated values) and
JSON (JavaScript Object Notation) pairs, and assembles a master record
table.

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
