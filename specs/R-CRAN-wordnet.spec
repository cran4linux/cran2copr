%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wordnet
%global packver   0.1-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.17
Release:          1%{?dist}%{?buildtag}
Summary:          WordNet Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       wordnet
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.6.3
Requires:         R-CRAN-rJava >= 0.6.3

%description
An interface to WordNet using the Jawbone Java API to WordNet. WordNet
(<https://wordnet.princeton.edu/>) is a large lexical database of English.
Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive
synonyms (synsets), each expressing a distinct concept.  Synsets are
interlinked by means of conceptual-semantic and lexical relations. Please
note that WordNet(R) is a registered tradename.  Princeton University
makes WordNet available to research and commercial users free of charge
provided the terms of their license
(<https://wordnet.princeton.edu/license-and-commercial-use>) are followed,
and proper reference is made to the project using an appropriate citation
(<https://wordnet.princeton.edu/citing-wordnet>). The WordNet database
files need to be made available separately, either via package
'wordnetDicts' from <https://datacube.wu.ac.at>, installing system
packages where available, or direct download from
<https://wordnetcode.princeton.edu/3.0/WNdb-3.0.tar.gz>.

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
