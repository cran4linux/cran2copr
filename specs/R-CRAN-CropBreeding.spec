%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CropBreeding
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stability Analysis in Crop Breeding

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-metan 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-metan 
Requires:         R-CRAN-rlang 

%description
Provides tools for crop breeding analysis including Genetic Coefficient of
Variation (GCV), Phenotypic Coefficient of Variation (PCV), heritability,
genetic advance calculations, stability analysis using the
Eberhart-Russell model, two-way ANOVA for genotype-environment
interactions, and Additive Main Effects and Multiplicative Interaction
(AMMI) analysis. These tools are developed for crop breeding research and
stability evaluation under various environmental conditions. The methods
are based on established statistical and biometrical principles. Refer to
Eberhart and Russell (1966)
<doi:10.2135/cropsci1966.0011183X000600010011x> for stability parameters,
Fisher (1935) "The Design of Experiments" <ISBN:9780198522294>, Falconer
(1996) "Introduction to Quantitative Genetics" <ISBN:9780582243026>, and
Singh and Chaudhary (1985) "Biometrical Methods in Quantitative Genetic
Analysis" <ISBN:9788122433764> for foundational methodologies.

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
