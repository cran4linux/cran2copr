%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cpp11tesseract
%global packver   5.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Open Source OCR Engine

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-digest 

%description
Bindings to 'tesseract': 'tesseract'
(<https://github.com/tesseract-ocr/tesseract>) is a powerful optical
character recognition (OCR) engine that supports over 100 languages. The
engine is highly configurable in order to tune the detection algorithms
and obtain the best possible results.

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
