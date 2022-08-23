%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PsychWordVec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Word Embedding Research Framework for Psychological Science

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bruceR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-rsparse 
BuildRequires:    R-CRAN-text2vec 
BuildRequires:    R-CRAN-word2vec 
BuildRequires:    R-CRAN-fastTextR 
Requires:         R-CRAN-bruceR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-rsparse 
Requires:         R-CRAN-text2vec 
Requires:         R-CRAN-word2vec 
Requires:         R-CRAN-fastTextR 

%description
An integrated toolkit of word embedding research that provides: (1) a
collection of 'pre-trained' word vectors in the '.RData' compressed format
<https://psychbruce.github.io/WordVector_RData.pdf>; (2) a variety of
functions to process, analyze, and visualize word vectors; (3) a range of
tests to examine conceptual associations, including the Word Embedding
Association Test <doi:10.1126/science.aal4230> and the Relative Norm
Distance <doi:10.1073/pnas.1720347115>; (4) a set of training methods to
locally train word vectors from text corpora, including 'Word2Vec'
<arXiv:1301.3781>, 'GloVe' <doi:10.3115/v1/D14-1162>, and 'FastText'
<arXiv:1607.04606>.

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
