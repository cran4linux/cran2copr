%global packname  spectral
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Common Methods of Spectral Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rasterImage 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-rasterImage 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-pbapply 

%description
On discrete data spectral analysis is performed by Fourier and Hilbert
transforms as well as with model based analysis called Lomb-Scargle
method. Fragmented and irregularly spaced data can be processed in almost
all methods. Both, FFT as well as LOMB methods take multivariate data and
return standardized PSD. For didactic reasons an analytical approach for
deconvolution of noise spectra and sampling function is provided. A user
friendly interface helps to interpret the results.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
