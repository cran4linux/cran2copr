%global packname  pould
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phased or Unphased Linkage Disequilibrium

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haplo.stats 
BuildRequires:    R-CRAN-gap 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-BIGDAWG 
BuildRequires:    R-graphics 
Requires:         R-CRAN-haplo.stats 
Requires:         R-CRAN-gap 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-BIGDAWG 
Requires:         R-graphics 

%description
Computes the D', Wn, and conditional asymmetric linkage disequilibrium
(ALD) measures for pairs of genetic loci. Performs these linkage
disequilibrium (LD) calculations on phased genotype data recorded using
Genotype List (GL) String or columnar formats. Alternatively, generates
expectation-maximization (EM) estimated haplotypes from phased data, or
performs LD calculations on EM estimated haplotypes. Performs sign tests
comparing LD values for phased and unphased datasets, and generates
heat-maps for each LD measure. Described by Osoegawa et al. (2019a)
<doi:10.1016/j.humimm.2019.01.010>, and Osoegawa et. al. (2019b)
<doi:10.1016/j.humimm.2019.05.018>.

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
