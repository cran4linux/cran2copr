%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spell.replacer
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Spelling Correction in a Character Vector

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-textclean 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-textclean 

%description
Automatically replaces "misspelled" words in a character vector based on
their string distance from a list of words sorted by their frequency in a
corpus. The default word list provided in the package comes from the
Corpus of Contemporary American English. Uses the Jaro-Winkler distance
metric for string similarity as implemented in van der Loo (2014)
<doi:10.32614/RJ-2014-011>. The word frequency data is derived from Davies
(2008-) "The Corpus of Contemporary American English (COCA)"
<https://www.english-corpora.org/coca/>.

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
