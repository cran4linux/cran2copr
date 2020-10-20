%global packname  fulltext
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Full Text of 'Scholarly' Articles Across Many Data Sources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-rentrez >= 1.1.0
BuildRequires:    R-CRAN-rplos >= 0.8.0
BuildRequires:    R-CRAN-rcrossref >= 0.8.0
BuildRequires:    R-CRAN-crul >= 0.7.0
BuildRequires:    R-CRAN-hoardr >= 0.5.0
BuildRequires:    R-CRAN-crminer >= 0.2.0
BuildRequires:    R-CRAN-microdemic >= 0.2.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-aRxiv 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-storr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fauxpas 
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-rentrez >= 1.1.0
Requires:         R-CRAN-rplos >= 0.8.0
Requires:         R-CRAN-rcrossref >= 0.8.0
Requires:         R-CRAN-crul >= 0.7.0
Requires:         R-CRAN-hoardr >= 0.5.0
Requires:         R-CRAN-crminer >= 0.2.0
Requires:         R-CRAN-microdemic >= 0.2.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-aRxiv 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-storr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fauxpas 

%description
Provides a single interface to many sources of full text 'scholarly' data,
including 'Biomed Central', Public Library of Science, 'Pubmed Central',
'eLife', 'F1000Research', 'PeerJ', 'Pensoft', 'Hindawi', 'arXiv'
'preprints', and more. Functionality included for searching for articles,
downloading full or partial text, downloading supplementary materials,
converting to various data formats.

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
