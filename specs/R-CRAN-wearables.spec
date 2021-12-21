%global __brp_check_rpaths %{nil}
%global packname  wearables
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Read and Convert Wearables Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RHRV 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-padr 
BuildRequires:    R-CRAN-varian 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RHRV 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-padr 
Requires:         R-CRAN-varian 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-R.utils 

%description
Package to read Empatica E4 data, perform several transformations, perform
signal processing and analyses, including batch analyses.

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
