%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  serad
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Standardized Economic Reporting and Automated Dynamic Writing / Synthèse d'Écrits Avec des Règles Automatisées et Dynamiques

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-tibble 

%description
Provides tools for generating dynamic and standardized economic narratives
in R Markdown documents. The package is primarily designed for
French-language statistical and economic publications. It includes
functions to describe changes in levels, percentages, trends,
accelerations and short-term economic developments using consistent
linguistic rules. The package supports automated reporting workflows and
reproducible economic writing. Fournit des outils permettant de générer
des textes économiques dynamiques et standardisés dans des documents R
Markdown. Le package est principalement conçu pour les publications
statistiques et économiques en français. Il propose des fonctions
permettant de décrire les évolutions de niveaux, de pourcentages, de
tendances, d'accélérations et les évolutions conjoncturelles à l'aide de
règles linguistiques homogènes. Le package facilite l'automatisation de la
rédaction et la reproductibilité des publications économiques.

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
