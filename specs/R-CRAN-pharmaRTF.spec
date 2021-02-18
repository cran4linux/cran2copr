%global packname  pharmaRTF
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Enhanced RTF Wrapper for Use with Existing Table Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-huxtable >= 4.7.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-huxtable >= 4.7.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-assertthat >= 0.2.1

%description
Enhanced RTF wrapper written in R for use with existing R tables packages
such as 'Huxtable' or 'GT'. This package fills a gap where tables in
certain packages can be written out to RTF, but cannot add certain
metadata or features to the document that are required/expected in a
report for a regulatory submission, such as multiple levels of titles and
footnotes, making the document landscape, and controlling properties such
as margins.

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
