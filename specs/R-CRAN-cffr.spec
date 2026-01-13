%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cffr
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Citation File Format ('cff') Metadata for R Packages

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.7.2
BuildRequires:    R-CRAN-desc >= 1.3.0
BuildRequires:    R-CRAN-jsonvalidate >= 1.1.0
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.7.2
Requires:         R-CRAN-desc >= 1.3.0
Requires:         R-CRAN-jsonvalidate >= 1.1.0

%description
The Citation File Format version 1.2.0 <doi:10.5281/zenodo.5171937> is a
human and machine readable file format which provides citation metadata
for software. This package provides core utilities to generate and
validate this metadata.

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
