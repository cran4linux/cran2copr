%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DEploid
%global packver   0.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          Deconvolute Mixed Genomes with Unknown Proportions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-rmarkdown >= 1.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-htmlwidgets >= 1.0
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-DEploid.utils >= 0.0.1
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-rmarkdown >= 1.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-htmlwidgets >= 1.0
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-DEploid.utils >= 0.0.1

%description
Traditional phasing programs are limited to diploid organisms. Our method
modifies Li and Stephens algorithm with Markov chain Monte Carlo (MCMC)
approaches, and builds a generic framework that allows haplotype searches
in a multiple infection setting. This package is primarily developed as
part of the Pf3k project, which is a global collaboration using the latest
sequencing technologies to provide a high-resolution view of natural
variation in the malaria parasite Plasmodium falciparum. Parasite DNA are
extracted from patient blood sample, which often contains more than one
parasite strain, with unknown proportions. This package is used for
deconvoluting mixed haplotypes, and reporting the mixture proportions from
each sample.

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
