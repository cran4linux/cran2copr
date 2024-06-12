%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppgm
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          PaleoPhyloGeographic Modeling of Climate Niches and Species Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-geiger 
Requires:         R-methods 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-stringi 

%description
Reconstruction of paleoclimate niches using phylogenetic comparative
methods and projection reconstructed niches onto paleoclimate maps. The
user can specify various models of trait evolution or estimate the best
fit model, include fossils, use one or multiple phylogenies for inference,
and make animations of shifting suitable habitat through time. This model
was first used in Lawing and Polly (2011), and further implemented in
Lawing et al (2016) and Rivera et al (2020). Lawing and Polly (2011)
<doi:10.1371/journal.pone.0028554> "Pleistocene climate, phylogeny and
climate envelope models: An integrative approach to better understand
species' response to climate change" Lawing et al (2016)
<doi:10.1086/687202> "Including fossils in phylogenetic climate
reconstructions: A deep time perspective on the climatic niche evolution
and diversification of spiny lizards (Sceloporus)" Rivera et al (2020)
<doi:10.1111/jbi.13915> "Reconstructing historical shifts in suitable
habitat of Sceloporus lineages using phylogenetic niche modelling.".

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
