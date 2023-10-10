%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fuzzySim
%global packver   4.10.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.10.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fuzzy Similarity in Species Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-modEvA > 3.9
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-modEvA > 3.9
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions to compute fuzzy versions of species occurrence patterns based
on presence-absence data (including inverse distance interpolation, trend
surface analysis, and prevalence-independent favourability obtained from
probability of presence), as well as pair-wise fuzzy similarity (based on
fuzzy logic versions of commonly used similarity indices) among those
occurrence patterns. Includes also functions for model consensus and
comparison (overlap and fuzzy similarity, loss or gain), and for data
preparation, such as obtaining unique abbreviations of species names,
cleaning and gridding (thinning) point occurrence data onto raster maps,
selecting absences under specified criteria, converting species lists
(long format) to presence-absence tables (wide format), transposing part
of a data frame, selecting relevant variables for models, assessing the
false discovery rate, or analysing and dealing with multicollinearity.
Initially described in Barbosa (2015) <doi:10.1111/2041-210X.12372>.

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
