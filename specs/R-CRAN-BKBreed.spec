%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BKBreed
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Colourful Biometrical Analysis for Plant Breeding and Genetics

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
A compact, colour-first toolkit for the analysis of plant breeding and
genetics field experiments. It provides analysis of variance for the
randomised block design (RBD) and factorial RBD, a check-anchored
intra-block analysis for augmented alpha-lattice designs, and the core
biometrical-genetics workflow used in crop improvement: estimation of
genetic variability (genotypic and phenotypic coefficients of variation,
broad-sense heritability, expected genetic advance), genotypic and
phenotypic correlation, path-coefficient analysis, line x tester and
Griffing diallel combining-ability analysis (general combining ability and
specific combining ability), Mahalanobis D-square genetic-divergence
analysis with Tocher and hierarchical clustering, and
genotype-by-environment stability analysis (Eberhart-Russell regression
and the additive main effects and multiplicative interaction (AMMI)
model). Methods follow Griffing (1956) <doi:10.1071/BI9560463> and
Eberhart and Russell (1966)
<doi:10.2135/cropsci1966.0011183X000600010011x>. Every analysis returns a
tidy result object and a publication-ready 'ggplot2' figure using a
bespoke high-contrast colour system.

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
