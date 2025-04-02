%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  orloca.es
%global packver   5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Spanish version of orloca package. Modelos de localizacion en investigacion operativa

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-orloca >= 5.3
Requires:         R-CRAN-orloca >= 5.3

%description
Help and demo in Spanish of the orloca package. Ayuda y demo en espanol
del paquete orloca. Objetos y metodos para manejar y resolver el problema
de localizacion de suma minima, tambien conocido como problema de
Fermat-Weber. El problema de localizacion de suma minima busca un punto
tal que la suma ponderada de las distancias a los puntos de demanda se
minimice. Vease "The Fermat-Weber location problem revisited" por
Brimberg, Mathematical Programming, 1, pag. 71-76, 1995. <DOI:
10.1007/BF01592245>. Se usan algoritmos generales de optimizacion global
para resolver el problema, junto con el metodo especifico Weiszfeld, vease
"Sur le point pour lequel la Somme des distance de n points donnes est
minimum", por Weiszfeld, Tohoku Mathematical Journal, First Series, 43,
pag. 355-386, 1937 o "On the point for which the sum of the distances to n
given points is minimum", por E. Weiszfeld y F. Plastria, Annals of
Operations Research, 167, pg. 7-41, 2009. <DOI:10.1007/s10479-008-0352-z>.

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
