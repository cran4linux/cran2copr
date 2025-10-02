%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PhytoIn
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vegetation Analysis and Forest Inventory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-packcircles 
BuildRequires:    R-CRAN-BIOMASS 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-packcircles 
Requires:         R-CRAN-BIOMASS 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-stats 

%description
Provides functions and example datasets for phytosociological analysis,
forest inventory, biomass and carbon estimation, and visualization of
vegetation data. Includes functions to compute structural parameters
[phytoparam(), summary.param(), stats()], estimate above-ground biomass
and carbon [AGB()], stratify wood volume by diameter at breast height
(DBH) classes [stratvol()], generate collector and rarefaction curves
[collector.curve(), rarefaction()], and visualize basal areas on quadrat
maps [BAplot(), including rectangular plots and individual coordinates].
Several example datasets are provided to demonstrate the functionality of
these tools. For more details see FAO (1981, ISBN:92-5-101132-X) "Manual
of forest inventory", IBGE (2012, ISBN:9788524042720) "Manual técnico da
vegetação brasileira" and Heringer et al. (2020) "Phytosociology in R: A
routine to estimate phytosociological parameters"
<doi:10.22533/at.ed.3552009033>.

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
