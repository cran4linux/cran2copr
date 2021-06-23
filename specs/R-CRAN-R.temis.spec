%global __brp_check_rpaths %{nil}
%global packname  R.temis
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Integrated Text Mining Solution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-explor 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-tm.plugin.factiva 
BuildRequires:    R-CRAN-tm.plugin.lexisnexis 
BuildRequires:    R-CRAN-tm.plugin.europresse 
BuildRequires:    R-CRAN-tm.plugin.alceste 
Requires:         R-CRAN-tm >= 0.6
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-explor 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-tm.plugin.factiva 
Requires:         R-CRAN-tm.plugin.lexisnexis 
Requires:         R-CRAN-tm.plugin.europresse 
Requires:         R-CRAN-tm.plugin.alceste 

%description
An integrated solution to perform a series of text mining tasks such as
importing and cleaning a corpus, and analyses like terms and documents
counts, lexical summary, terms co-occurrences and documents similarity
measures, graphs of terms, correspondence analysis and hierarchical
clustering. Corpora can be imported from spreadsheet-like files,
directories of raw text files, as well as from 'Dow Jones Factiva',
'LexisNexis', 'Europresse' and 'Alceste' files.

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
