%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  namedropR
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create Visual Citations for Presentations and Posters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-qrcode >= 0.1.4
BuildRequires:    R-CRAN-bib2df 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-qrcode >= 0.1.4
Requires:         R-CRAN-bib2df 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-webshot 

%description
Provides 'visual citations' containing the metadata of a scientific paper
and a 'QR' code.  A 'visual citation' is a banner containing title,
authors, journal and year of a publication.  This package can create such
banners based on 'BibTeX' and 'BibLaTeX' references or call the reference
metadata from 'Crossref'-API. The banners include a QR code pointing to
the 'DOI'.  The resulting HTML object or PNG image can be included in a
presentation to point the audience to good resources for further reading.
Styling is possible via predefined designs or via custom 'CSS'.  This
package is not intended as replacement for proper reference manager
packages, but a tool to enrich scientific presentation slides and
conference posters.

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
