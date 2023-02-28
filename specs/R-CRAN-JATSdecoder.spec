%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JATSdecoder
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Metadata and Text Extraction and Manipulation Tool Set

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-openNLP 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-openNLP 

%description
Provides a function collection to extract metadata, sectioned text and
study characteristics from scientific articles in 'NISO-JATS' format.
Articles in PDF format can be converted to 'NISO-JATS' with the 'Content
ExtRactor and MINEr' ('CERMINE', <https://github.com/CeON/CERMINE>). For
convenience, two functions bundle the extraction heuristics: JATSdecoder()
converts 'NISO-JATS'-tagged XML files to a structured list with elements
title, author, journal, history, 'DOI', abstract, sectioned text and
reference list. study.character() extracts multiple study characteristics
like number of included studies, statistical methods used, alpha error,
power, statistical results, correction method for multiple testing,
software used. An estimation of the involved sample size is performed
based on reports within the abstract and the reported degrees of freedom
within statistical results. In addition, the package contains some useful
functions to process text (text2sentences(), text2num(), ngram(),
strsplit2(), grep2()). See Böschen, I. (2021)
<doi:10.1007/s11192-021-04162-z> Böschen, I. (2021)
<doi:10.1038/s41598-021-98782-3> and Böschen, I (2023)
<doi:10.1038/s41598-022-27085-y>.

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
