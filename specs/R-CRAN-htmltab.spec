%global __brp_check_rpaths %{nil}
%global packname  htmltab
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assemble Data Frames from HTML Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.3
BuildRequires:    R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-XML >= 3.98.1.3
Requires:         R-CRAN-httr >= 1.0.0

%description
HTML tables are a valuable data source but extracting and recasting these
data into a useful format can be tedious. This package allows to collect
structured information from HTML tables. It is similar to
`readHTMLTable()` of the XML package but provides three major advantages.
First, the function automatically expands row and column spans in the
header and body cells. Second, users are given more control over the
identification of header and body rows which will end up in the R table,
including semantic header information that appear throughout the body.
Third, the function preprocesses table code, corrects common types of
malformations, removes unneeded parts and so helps to alleviate the need
for tedious post-processing.

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
