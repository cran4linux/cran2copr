%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NUETON
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nitrogen Use Efficiency Toolkit on Numerics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Comprehensive R package designed to facilitate the calculation of Nitrogen
Use Efficiency (NUE) indicators using experimentally derived data. The
package incorporates 23 parameters categorized into six fertilizer-based,
four plant-based, three soil-based, three isotope-based, two
ecology-based, and four system-based indicators, providing a versatile
platform for NUE assessment. As of the current version, 'NUETON' serves as
a starting point for users to compute NUE indicators from their
experimental data. Future updates are planned to enhance the package's
capabilities, including robust data visualization tools and error margin
consideration in calculations. Additionally, statistical methods will be
integrated to ensure the accuracy and reliability of the calculated
indicators. All formulae used in 'NUETON' are thoroughly referenced within
the source code, and the package is released as open source software.
Users are encouraged to provide feedback and contribute to the improvement
of this package. It is important to note that the current version of
'NUETON' is not intended for rigorous research purposes, and users are
responsible for validating their results. The package developers do not
assume liability for any inaccuracies in calculations. This package
includes content from Congreves KA, Otchere O, Ferland D, Farzadfar S,
Williams S and Arcand MM (2021) 'Nitrogen Use Efficiency Definitions of
Today and Tomorrow.' Front. Plant Sci. 12:637108.
<doi:10.3389/fpls.2021.637108>. The article is available under the
Creative Commons Attribution License (CC BY) C. 2021 Congreves, Otchere,
Ferland, Farzadfar, Williams and Arcand.

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
