%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GCubeR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Forest Volume, Biomass, and Carbon

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 

%description
Provides tools for estimating forest metrics such as stem volume, biomass,
and carbon using regional allometric equations. The package implements
widely used models including Dagnelie P., Rondeux J. & Palm R. (2013,
ISBN:9782870161258) "Cubage des arbres et des peuplements forestiers -
Tables et equations" <https://orbi.uliege.be/handle/2268/155356>, Vallet
P., Dhote J.-F., Le Moguedec G., Ravart M. & Pignard G. (2006)
"Development of total aboveground volume equations for seven important
forest tree species in France" <doi:10.1016/j.foreco.2006.03.013>, Pauwels
D. & Rondeux J. (1999, ISSN:07779992) "Tarifs de cubage pour les petits
bois de meleze (Larix sp.) en Ardenne"
<https://orbi.uliege.be/handle/2268/96128>, Massenet J.-Y. (2006)
"Chapitre IV: Estimation du volume"
<https://jymassenet-foret.fr/cours/dendrometrie/Coursdendrometriepdf/Dendro4-2009.pdf>,
France Valley (2025) "Bilan Carbone Forestier - Methodologie"
<https://www.france-valley.com/hubfs/Bilan%%20Carbone%%20Forestier.pdf>. Its
modular structure allows transparent integration of bibliographic or
user-defined allometric relationships.

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
