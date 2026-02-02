%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  date4ts
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Wrangle and Modify Ts Object with Classic Frequencies and Exact Dates

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-stats 
Requires:         R-CRAN-checkmate 

%description
The ts objects in R are managed using a very specific date format (in the
form c(2022, 9) for September 2022 or c(2021, 2) for the second quarter of
2021, depending on the frequency, for example). We focus solely on monthly
and quarterly series to manage the dates of ts objects. The general idea
is to offer a set of functions to manage this date format without it being
too restrictive or too imprecise depending on the rounding. This is a
compromise between simplicity, precision and use of the basic 'stats'
functions for creating and managing time series (ts(), window()). Les
objets ts en R sont gérés par un format de date très particulier (sous la
forme c(2022, 9) pour septembre 2022 ou c(2021, 2) pour le deuxième
trimestre 2021 selon la fréquence par exemple). On se concentre uniquement
sur les séries mensuelles et trimestrielles pour gérer les dates des
objets ts. Lidée générale est de proposer un ensemble de fonctions pour
gérer ce format de date sans que ce soit trop contraignant ou trop
imprécis selon les arrondis. Cest un compromis entre simplicité, précision
et utilisation des fonctions du package 'stats' de création et de gestion
des séries temporelles (ts(), window()).

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
