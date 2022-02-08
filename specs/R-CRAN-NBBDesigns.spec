%global __brp_check_rpaths %{nil}
%global packname  NBBDesigns
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Neighbour Balanced Block Designs (NBBDesigns)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Neighbour-balanced designs ensure that no treatment is disadvantaged
unfairly by its surroundings. The treatment allocation in these designs is
such that every treatment appears equally often as a neighbour with every
other treatment. Neighbour Balanced Designs are employed when there is a
possibility of neighbour effects from treatments used in adjacent
experimental units. In the literature, a vast number of such designs have
been developed. This package generates some efficient neighbour balanced
block designs which are balanced and partially variance balanced for
estimating the contrast pertaining to direct and neighbour effects, as
well as provides a function for analysing the data obtained from such
trials (Azais, J.M., Bailey, R.A. and Monod, H. (1993). "A catalogue of
efficient neighbour designs with border plots". Biometrics, 49, 1252-1261
; Tomar, J. S., Jaggi, Seema and Varghese, Cini (2005)<DOI:
10.1080/0266476042000305177>. "On totally balanced block designs for
competition effects"). This package contains functions named
nbbd1(),nbbd2(),nbbd3(),pnbbd1() and pnbbd2() which generates neighbour
balanced block designs within a specified range of number of treatment
(v). It contains another function named anlys()for performing the analysis
of data generated from such trials.

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
