%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  unexcel
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Revert Spreadsheet Date Auto-Conversion to the Numbers Typed

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.3.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-xml2 >= 1.3.0
Requires:         R-stats 
Requires:         R-utils 

%description
Spreadsheets silently turn entries such as '30.3' into dates, so the
imported data carry date serials instead of the numbers that were typed.
Reading the workbook directly recovers those numbers without guesswork: an
'xlsx' file states its own date system, and records which cells are
formatted as dates and in which field order, so the values to repair are
identified from the file rather than inferred from their magnitude.
Functions are also provided for data already imported, where that evidence
is no longer available, using conservative and configurable detection.

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
