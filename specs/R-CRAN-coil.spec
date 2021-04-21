%global packname  coil
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Contextualization and Evaluation of COI-5P Barcode Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-aphid 
BuildRequires:    R-CRAN-seqinr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-aphid 
Requires:         R-CRAN-seqinr 

%description
Designed for the cleaning, contextualization and assessment of cytochrome
c oxidase I DNA barcode data (COI-5P, or the five prime portion of COI).
It contains functions for placing COI-5P barcode sequences into a common
reading frame, translating DNA sequences to amino acids and for assessing
the likelihood that a given barcode sequence includes an insertion or
deletion error. The error assessment relies on the comparison of input
sequences against nucleotide and amino acid profile hidden Markov models
(PHMMs) (for details see Durbin et al. 1998, ISBN: 9780521629713) trained
on a taxonomically diverse set of reference sequences. The functions are
provided as a complete pipeline and are also available individually for
efficient and targeted analysis of barcode data.

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
