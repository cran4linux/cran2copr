%global packname  vprr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Processing and Visualization of Visual Plankton Recorder Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-oce 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-gsw 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-oce 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-gsw 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-usethis 

%description
An oceanographic data processing package for analyzing and visualizing
Video Plankton Recorder data. Works in concert with Visual Plankton
(MATLAB) software developed at 'WHOI'. This package was developed at
'Bedford Institute of Oceanography'. Functions are designed to process
Visual Plankton output and create organized and easily portable data
products.

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
