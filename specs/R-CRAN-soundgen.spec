%global packname  soundgen
%global packver   1.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sound Synthesis and Acoustic Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-seewave >= 2.1.0
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-phonTools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-seewave >= 2.1.0
Requires:         R-CRAN-shinyBS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-phonTools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 

%description
Performs parametric synthesis of sounds with harmonic and noise components
such as animal vocalizations or human voice. Also offers tools for
spectral analysis, audio segmentation, self-similarity matrices,
modulation spectra, morphing, etc., as well as interactive web apps for
manually corrected pitch tracking and formant measurement. Reference:
Anikin (2019) <doi:10.3758/s13428-018-1095-7>.

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
