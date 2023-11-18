%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ohun
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimizing Acoustic Signal Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-seewave >= 2.0.1
BuildRequires:    R-CRAN-warbleR >= 1.1.29
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-seewave >= 2.0.1
Requires:         R-CRAN-warbleR >= 1.1.29
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-fftw 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 

%description
Facilitates the automatic detection of acoustic signals, providing
functions to diagnose and optimize the performance of detection routines.
Detections from other software can also be explored and optimized.
Araya-Salas et al. (2022) <doi:10.1101/2022.12.13.520253>.

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
