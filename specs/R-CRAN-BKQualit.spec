%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BKQualit
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Qualitative Traits, Segregation and Genetic Linkage

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 

%description
A colour-first toolkit for the analysis of qualitative (categorical)
traits in plant breeding and genetics. It tests observed segregation
against the classical Mendelian expectations, fitting every standard
mono-, di- and trihybrid ratio automatically and ranking them by goodness
of fit, with Yates continuity correction and Monte Carlo exact tests for
sparse tables. It partitions chi-square across families into pooled and
heterogeneity components, so that a poor overall fit can be attributed
either to the hypothesised ratio or to variation between families. Genetic
linkage is estimated by maximum likelihood from two-locus second filial
generation and backcross data, with logarithm of odds scores and
likelihood-ratio confidence intervals for the recombination fraction. The
package further computes Shannon-Weaver and Simpson diversity for
descriptor states used in distinctness, uniformity and stability testing,
and performs multiple correspondence analysis and Gower-distance
clustering of mixed categorical and quantitative descriptors. Every
analysis returns a tidy result object and a publication-ready 'ggplot2'
figure. Methods follow Mather (1951, <ISBN:9780416470406>), Allard (1956)
<doi:10.3733/hilg.v24n10p235> and Gower (1971) <doi:10.2307/2528823>.

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
