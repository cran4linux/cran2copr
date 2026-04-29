%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PGaovR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Experimental Data using ANOVA and Mean Comparison

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-multcompView 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for designing and analyzing agricultural experiments. It
includes functions for generating randomized treatment layouts for
standard experimental designs such as Completely Randomized Design (CRD),
Randomized Block Design (RBD), Latin Square Design (LSD), Factorial
Randomized Block Design (FRBD), split-plot design, and strip-plot design.
The package implements one-factor and two-factor analysis of variance
(ANOVA) and offers multiple comparison procedures, including Least
Significant Difference (LSD), Tukey, and Duncan tests, to compare
treatment means in single-factor and factorial experiments. The methods
follow classical experimental design principles described in Gomez and
Gomez (1984, Statistical Procedures for Agricultural Research, John Wiley
& Sons, New York).

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
