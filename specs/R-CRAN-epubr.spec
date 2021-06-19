%global packname  epubr
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Read EPUB File Metadata and Text

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xslt 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xslt 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Provides functions supporting the reading and parsing of internal e-book
content from EPUB files. The 'epubr' package provides functions supporting
the reading and parsing of internal e-book content from EPUB files. E-book
metadata and text content are parsed separately and joined together in a
tidy, nested tibble data frame. E-book formatting is not completely
standardized across all literature. It can be challenging to curate parsed
e-book content across an arbitrary collection of e-books perfectly and in
completely general form, to yield a singular, consistently formatted
output. Many EPUB files do not even contain all the same pieces of
information in their respective metadata. EPUB file parsing functionality
in this package is intended for relatively general application to
arbitrary EPUB e-books. However, poorly formatted e-books or e-books with
highly uncommon formatting may not work with this package. There may even
be cases where an EPUB file has DRM or some other property that makes it
impossible to read with 'epubr'. Text is read 'as is' for the most part.
The only nominal changes are minor substitutions, for example curly quotes
changed to straight quotes. Substantive changes are expected to be
performed subsequently by the user as part of their text analysis.
Additional text cleaning can be performed at the user's discretion, such
as with functions from packages like 'tm' or 'qdap'.

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
