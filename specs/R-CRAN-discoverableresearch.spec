%global packname  discoverableresearch
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Checks Title, Abstract and Keywords to Optimise Discoverability

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ngram 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-synthesisr 
BuildRequires:    R-CRAN-tm 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ngram 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-synthesisr 
Requires:         R-CRAN-tm 

%description
A suite of tools are provided here to support authors in making their
research more discoverable. check_keywords() - this function checks the
keywords to assess whether they are already represented in the title and
abstract. check_fields() - this function compares terminology used across
the title, abstract and keywords to assess where terminological diversity
(i.e. the use of synonyms) could increase the likelihood of the record
being identified in a search. The function looks for terms in the title
and abstract that also exist in other fields and highlights these as
needing attention. suggest_keywords() - this function takes a full text
document and produces a list of unigrams, bigrams and trigrams (1-, 2- or
2-word phrases) present in the full text after removing stop words (words
with a low utility in natural language processing) that do not occur in
the title or abstract that may be suitable candidates for keywords.
suggest_title() - this function takes a full text document and produces a
list of the most frequently used unigrams, bigrams and trigrams after
removing stop words that do not occur in the abstract or keywords that may
be suitable candidates for title words. check_title() - this function
carries out a number of sub tasks: 1) it compares the length (number of
words) of the title with the mean length of titles in major bibliographic
databases to assess whether the title is likely to be too short; 2) it
assesses the proportion of stop words in the title to highlight titles
with low utility in search engines that strip out stop words; 3) it
compares the title with a given sample of record titles from an .ris
import and calculates a similarity score based on phrase overlap. This
highlights the level of uniqueness of the title. This version of the
package also contains functions currently in a non-CRAN package called
'litsearchr' <https://github.com/elizagrames/litsearchr>.

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
