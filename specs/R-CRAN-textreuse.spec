%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  textreuse
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Detect Text Reuse and Document Similarity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-digest >= 0.6.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-NLP >= 0.1.8
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-digest >= 0.6.8
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-NLP >= 0.1.8
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-CRAN-Matrix 

%description
Tools for measuring similarity among documents and detecting passages
which have been reused. Implements shingled n-gram, skip n-gram, and other
tokenizers; similarity/dissimilarity functions; pairwise comparisons;
minhash and locality sensitive hashing algorithms; and a version of the
Smith-Waterman local alignment algorithm suitable for natural language.

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
