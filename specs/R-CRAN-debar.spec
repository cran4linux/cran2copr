%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  debar
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Post-Clustering Denoiser for COI-5P Barcode Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-aphid 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-aphid 
Requires:         R-CRAN-seqinr 
Requires:         R-parallel 

%description
The 'debar' sequence processing pipeline is designed for denoising high
throughput sequencing data for the animal DNA barcode marker cytochrome c
oxidase I (COI). The package is designed to detect and correct insertion
and deletion errors within sequencer outputs. This is accomplished through
comparison of input sequences against a profile hidden Markov model (PHMM)
using the Viterbi algorithm (for algorithm details see Durbin et al. 1998,
ISBN: 9780521629713). Inserted base pairs are removed and deleted base
pairs are accounted for through the introduction of a placeholder
character. Since the PHMM is a probabilistic representation of the COI
barcode, corrections are not always perfect. For this reason 'debar'
censors base pairs adjacent to reported indel sites, turning them into
placeholder characters (default is 7 base pairs in either direction, this
feature can be disabled). Testing has shown that this censorship results
in the correct sequence length being restored, and erroneous base pairs
being masked the vast majority of the time (>95%%).

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
