%global packname  act
%global packver   0.94
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.94
Release:          1%{?dist}%{?buildtag}
Summary:          Aligned Corpus Toolkit

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-openxlsx 

%description
The Aligned Corpus Toolkit (act) is designed for linguists that work with
time aligned transcription data. It offers advanced search possibilities
in transcriptions (full text search, normalized search, concordance etc.),
functions to modify the data, import-export functionality for 'Praat'
'*.TextGrid' files, export for 'ELAN' '*.eaf' files, the creation of batch
lists for cutting audio and video files with 'FFmpeg', the creation of
printable transcripts in the style of conversation analysis, and
interaction with 'Praat' using 'Praat'-scripts. The package is itself
written in R and may be expanded by other users.

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
