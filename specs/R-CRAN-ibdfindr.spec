%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ibdfindr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          HMM Toolkit for Inferring IBD Segments from SNP Genotypes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-forrel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ibdsim2 
BuildRequires:    R-CRAN-pedtools 
BuildRequires:    R-CRAN-ribd 
Requires:         R-CRAN-forrel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ibdsim2 
Requires:         R-CRAN-pedtools 
Requires:         R-CRAN-ribd 

%description
Implements continuous-time hidden Markov models (HMMs) to infer
identity-by-descent (IBD) segments shared by two individuals from their
single-nucleotide polymorphism (SNP) genotypes. Provides posterior
probabilities at each marker (forward-backward algorithm), prediction of
IBD segments (Viterbi algorithm), and functions for visualising results.
Supports both autosomal data and X-chromosomal data.

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
