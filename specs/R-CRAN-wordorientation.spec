%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wordorientation
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detect Attraction and Repulsion Between Words in Text

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-scales 

%description
Provides tools to quantify how strongly pairs of words attract or repel
each other in a text corpus, based on co-occurrence patterns. For each
word pair, the phi coefficient (a correlation measure for binary
variables) is computed from a document-term matrix and tested for
significance, then classified as showing attraction (co-occurring more
than chance would predict), repulsion (co-occurring less than chance would
predict), or no significant relationship. A full pipeline is provided from
raw text to a labeled network visualization. Unlike general-purpose
pairwise correlation tools, 'wordorientation' is built specifically for
text: it handles tokenization and stopword removal, applies
significance-based classification rather than reporting a raw correlation
coefficient alone, and produces a ready-to-plot attraction/ repulsion
network.

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
