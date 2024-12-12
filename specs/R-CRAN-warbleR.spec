%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  warbleR
%global packver   1.1.33
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.33
Release:          1%{?dist}%{?buildtag}
Summary:          Streamline Bioacoustic Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-seewave >= 2.0.1
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-NatureSounds 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-monitoR 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-bioacoustics 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-CRAN-seewave >= 2.0.1
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-NatureSounds 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-fftw 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-monitoR 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rjson 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-bioacoustics 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 

%description
Functions aiming to facilitate the analysis of the structure of animal
acoustic signals in 'R'. 'warbleR' makes use of the basic sound analysis
tools from the packages 'tuneR' and 'seewave', and offers new tools for
explore and quantify acoustic signal structure. The package allows to
organize and manipulate multiple sound files, create spectrograms of
complete recordings or individual signals in different formats, run
several measures of acoustic structure, and characterize different
structural levels in acoustic signals.

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
