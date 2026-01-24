%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aphid
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis with Profile Hidden Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-kmer >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-stats 
Requires:         R-CRAN-kmer >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-graphics 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-qpdf 
Requires:         R-stats 

%description
Designed for the development and application of hidden Markov models and
profile HMMs for biological sequence analysis. Contains functions for
multiple and pairwise sequence alignment, model construction and parameter
optimization, file import/export, implementation of the forward, backward
and Viterbi algorithms for conditional sequence probabilities, tree-based
sequence weighting, and sequence simulation. Features a wide variety of
potential applications including database searching, gene-finding and
annotation, phylogenetic analysis and sequence classification. Based on
the models and algorithms described in Durbin et al (1998, ISBN:
9780521629713).

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
