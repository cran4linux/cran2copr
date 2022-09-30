%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psych
%global packver   2.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Procedures for Psychological, Psychometric, and Personality Research

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-mnormt 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-nlme 

%description
A general purpose toolbox for personality, psychometric theory and
experimental psychology.  Functions are primarily for multivariate
analysis and scale construction using factor analysis, principal component
analysis, cluster analysis and reliability analysis, although others
provide basic descriptive statistics. Item Response Theory is done using
factor analysis of tetrachoric and polychoric correlations. Functions for
analyzing data at multiple levels include within and between group
statistics, including correlations and factor analysis.  Functions for
simulating and testing particular item and test structures are included.
Several functions serve as a useful front end for structural equation
modeling.  Graphical displays of path diagrams, factor analysis and
structural equation models are created using basic graphics. Some of the
functions are written to support a book on psychometric theory as well as
publications in personality research. For more information, see the
<https://personality-project.org/r/> web page.

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
