%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datetimeoffset
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Datetimes with Optional UTC Offsets and/or Heterogeneous Time Zones

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-CRAN-clock 
BuildRequires:    R-methods 
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-CRAN-clock 
Requires:         R-methods 

%description
Supports import/export for a number of datetime string standards and R
datetime classes often including lossless re-export of any original
reduced precision including 'ISO 8601'
<https://en.wikipedia.org/wiki/ISO_8601> and 'pdfmark'
<https://opensource.adobe.com/dc-acrobat-sdk-docs/library/pdfmark/>
datetime strings. Supports local/global datetimes with optional UTC
offsets and/or (possibly heterogeneous) time zones with up to nanosecond
precision.

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
