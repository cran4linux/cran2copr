%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  voice
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Speaker Recognition, Voice Analysis and Mood Inference via Music Theory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-tabr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-wrassp 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-tabr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-wrassp 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-httr 

%description
Provides tools for audio data analysis, including feature extraction,
pitch detection, and speaker identification. Designed for voice research
and signal processing applications.

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
