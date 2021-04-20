%global packname  LSX
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Model for Semisupervised Text Analysis Based on Word Embeddings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda >= 2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quanteda.textstats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-CRAN-rsparse 
BuildRequires:    R-CRAN-proxyC 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-locfit 
Requires:         R-CRAN-quanteda >= 2.0
Requires:         R-methods 
Requires:         R-CRAN-quanteda.textstats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-rsvd 
Requires:         R-CRAN-rsparse 
Requires:         R-CRAN-proxyC 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-locfit 

%description
A word embeddings-based semisupervised model for document scaling Watanabe
(2020) <doi:10.1080/19312458.2020.1832976>. LSS allows users to analyze
large and complex corpora on arbitrary dimensions with seed words
exploiting efficiency of word embeddings (SVD, Glove). It can generate
word vectors on a users-provided corpus or incorporate a pre-trained word
vectors.

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
