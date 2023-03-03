%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  act
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Aligned Corpus Toolkit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-textutils 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-tools 
Requires:         R-CRAN-textutils 
Requires:         R-utils 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-openxlsx 

%description
The Aligned Corpus Toolkit (act) is designed for linguists that work with
time aligned transcription data. It offers functions to import and export
various annotation file formats ('ELAN' .eaf, 'EXMARaLDA .exb and 'Praat'
.TextGrid files), create print transcripts in the style of conversation
analysis, search transcripts (span searches across multiple annotations,
search in normalized annotations, make concordances etc.), export and
re-import search results (.csv and 'Excel' .xlsx format), create cuts for
the search results (print transcripts, audio/video cuts using 'FFmpeg' and
video sub titles in 'Subrib title' .srt format), modify the data in a
corpus (search/replace, delete, filter etc.), interact with 'Praat' using
'Praat'-scripts, and exchange data with the 'rPraat' package. The package
is itself written in R and may be expanded by other users.

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
