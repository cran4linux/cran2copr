%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  waywiser
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ergonomic Methods for Assessing Spatial Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spdep >= 1.1.9
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-spdep >= 1.1.9
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-fields 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-yardstick 

%description
Assessing predictive models of spatial data can be challenging, both
because these models are typically built for extrapolating outside the
original region represented by training data and due to potential
spatially structured errors, with "hot spots" of higher than expected
error clustered geographically due to spatial structure in the underlying
data. Methods are provided for assessing models fit to spatial data,
including approaches for measuring the spatial structure of model errors,
assessing model predictions at multiple spatial scales, and evaluating
where predictions can be made safely. Methods are particularly useful for
models fit using the 'tidymodels' framework. Methods include Moran's I
('Moran' (1950) <doi:10.2307/2332142>), Geary's C ('Geary' (1954)
<doi:10.2307/2986645>), Getis-Ord's G ('Ord' and 'Getis' (1995)
<doi:10.1111/j.1538-4632.1995.tb00912.x>), agreement coefficients from
'Ji' and Gallo (2006) (<doi: 10.14358/PERS.72.7.823>), agreement metrics
from 'Willmott' (1981) (<doi: 10.1080/02723646.1981.10642213>) and
'Willmott' 'et' 'al'. (2012) (<doi: 10.1002/joc.2419>), an implementation
of the area of applicability methodology from 'Meyer' and 'Pebesma' (2021)
(<doi:10.1111/2041-210X.13650>), and an implementation of multi-scale
assessment as described in 'Riemann' 'et' 'al'. (2010)
(<doi:10.1016/j.rse.2010.05.010>).

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
