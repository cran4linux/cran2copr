%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  carwatch
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Processing of 'CARWatch' Sampling Logs and Saliva Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-withr >= 3.0.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-fs >= 1.6.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-clock >= 0.7.0
BuildRequires:    R-CRAN-digest >= 0.6.0
BuildRequires:    R-CRAN-vctrs >= 0.6.0
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-withr >= 3.0.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-fs >= 1.6.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-clock >= 0.7.0
Requires:         R-CRAN-digest >= 0.6.0
Requires:         R-CRAN-vctrs >= 0.6.0
Requires:         R-CRAN-boot 
Requires:         R-grid 

%description
Import and reconstruct saliva-sampling studies recorded by the 'CARWatch'
application. Registration metadata and raw barcode events are converted
into auditable study days and scheduled sample positions using a two-pass
issue-review workflow. Functions assess sampling-time compliance, merge
laboratory saliva measurements, calculate response features, and create
quality-control visualizations. The application is described by Richer et
al. (2023) <doi:10.1016/j.psyneuen.2023.106073>.

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
