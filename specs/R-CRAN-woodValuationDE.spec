%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  woodValuationDE
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Wood Valuation Germany

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0

%description
Monetary valuation of wood in German forests (stumpage values), including
estimations of harvest quantities, wood revenues, and harvest costs. The
functions are sensitive to tree species, mean diameter of the harvested
trees, stand quality, and logging method. The functions include
estimations for the consequences of disturbances on revenues and costs.
The underlying assortment tables are taken from Offer and Staupendahl
(2018) with corresponding functions for salable and skidded volume derived
in Fuchs et al. (2023). Wood revenue and harvest cost functions were taken
from v. Bodelschwingh (2018). The consequences of disturbances refer to
Dieter (2001), Moellmann and Moehring (2017), and Fuchs et al. (2022a,
2022b). For the full references see documentation of the functions,
package README, and Fuchs et al. (2023). Apart from Dieter (2001) and
Moellmann and Moehring (2017), all functions and factors are based on data
from HessenForst, the forest administration of the Federal State of Hesse
in Germany.

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
