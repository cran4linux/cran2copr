%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SemanticDistance
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Semantic Distance Between Text Constituents

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lsa 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-textstem 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-textclean 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wesanderson 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lsa 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-textstem 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-textclean 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-wesanderson 

%description
Cleans and formats language transcripts guided by a series of
transformation options (e.g., lemmatize words, omit stopwords, split
strings across rows). 'SemanticDistance' computes two distinct metrics of
cosine semantic distance (experiential and embedding). These values
reflect pairwise cosine distance between different elements or chunks of a
language sample. 'SemanticDistance' can process monologues (e.g., stories,
ordered text), dialogues (e.g., conversation transcripts), word pairs
arrayed in columns, and unordered word lists. Users specify options for
how they wish to chunk distance calculations. These options include:
rolling ngram-to-word distance (window of n-words to each new word),
ngram-to-ngram distance (2-word chunk to the next 2-word chunk), pairwise
distance between words arrayed in columns, matrix comparisons (i.e., all
possible pairwise distances between words in an unordered list),
turn-by-turn distance (talker to talker in a dialogue transcript).
'SemanticDistance' includes visualization options for analyzing distances
as time series data and simple semantic network dynamics (e.g.,
clustering, undirected graph network).

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
