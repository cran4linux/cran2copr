%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  admetshiny
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive ADMET and Drug-Likeness Analysis of Small Molecules

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-fingerprint 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-rcdk 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-webchem 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-fingerprint 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-rcdk 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-webchem 

%description
Provides an interactive Shiny application and a toolbox of R functions for
the management, calculation, filtering, visualization and exploratory
analysis of molecular descriptors and ADMET (Absorption, Distribution,
Metabolism, Excretion and Toxicity) properties of small molecules.
Computes descriptors locally via the Chemistry Development Kit (CDK), and
offers drug-likeness filters (Lipinski, Veber, Ghose, Egan, Muegge), the
BOILED-Egg model for gastrointestinal absorption and blood-brain barrier
permeability, a P-glycoprotein (P-gp, also known as ATP-binding cassette
sub-family B member 1, ABCB1) substrate Random Forest classifier,
Principal Component Analysis (PCA), t-Distributed Stochastic Neighbor
Embedding (t-SNE), Uniform Manifold Approximation and Projection (UMAP),
radar plots and Tanimoto / AGglomerative NESting (AGNES) clustering to
support compound prioritization in early-stage drug discovery.

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
