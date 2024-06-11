%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spdep
%global packver   1.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Dependence: Weighting Schemes, Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-spData >= 2.3.1
BuildRequires:    R-CRAN-boot >= 1.3.1
BuildRequires:    R-CRAN-sp >= 1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-s2 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-spData >= 2.3.1
Requires:         R-CRAN-boot >= 1.3.1
Requires:         R-CRAN-sp >= 1.0
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-deldir 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-units 
Requires:         R-CRAN-s2 
Requires:         R-CRAN-e1071 

%description
A collection of functions to create spatial weights matrix objects from
polygon 'contiguities', from point patterns by distance and tessellations,
for summarizing these objects, and for permitting their use in spatial
data analysis, including regional aggregation by minimum spanning tree; a
collection of tests for spatial 'autocorrelation', including global
'Morans I' and 'Gearys C' proposed by 'Cliff' and 'Ord' (1973, ISBN:
0850860369) and (1981, ISBN: 0850860814), 'Hubert/Mantel' general cross
product statistic, Empirical Bayes estimates and 'Assunção/Reis' (1999)
<doi:10.1002/(SICI)1097-0258(19990830)18:16%%3C2147::AID-SIM179%%3E3.0.CO;2-I>
Index, 'Getis/Ord' G ('Getis' and 'Ord' 1992)
<doi:10.1111/j.1538-4632.1992.tb00261.x> and multicoloured join count
statistics, 'APLE' ('Li 'et al.' ) <doi:10.1111/j.1538-4632.2007.00708.x>,
local 'Moran's I', 'Gearys C' ('Anselin' 1995)
<doi:10.1111/j.1538-4632.1995.tb00338.x> and 'Getis/Ord' G ('Ord' and
'Getis' 1995) <doi:10.1111/j.1538-4632.1995.tb00912.x>, 'saddlepoint'
approximations ('Tiefelsdorf' 2002)
<doi:10.1111/j.1538-4632.2002.tb01084.x> and exact tests for global and
local 'Moran's I' ('Bivand et al.' 2009) <doi:10.1016/j.csda.2008.07.021>
and 'LOSH' local indicators of spatial heteroscedasticity ('Ord' and
'Getis') <doi:10.1007/s00168-011-0492-y>. The implementation of most of
these measures is described in 'Bivand' and 'Wong' (2018)
<doi:10.1007/s11749-018-0599-x>, with further extensions in 'Bivand'
(2022) <doi:10.1111/gean.12319>. 'Lagrange' multiplier tests for spatial
dependence in linear models are provided ('Anselin et al'. 1996)
<doi:10.1016/0166-0462(95)02111-6>, as are 'Rao' score tests for
hypothesised spatial 'Durbin' models based on linear models ('Koley' and
'Bera' 2023) <doi:10.1080/17421772.2023.2256810>. From 'spdep' and
'spatialreg' versions >= 1.2-1, the model fitting functions previously
present in this package are defunct in 'spdep' and may be found in
'spatialreg'.

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
