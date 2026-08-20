%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigbang
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build 'Tidyverse'-Style Meta-Packages from Local Package Files

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-brio 
Requires:         R-CRAN-glue 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-whisker 

%description
Turns a curated set of package archives (.tar.gz, .zip) into one
meta-package in the style of the 'tidyverse', so that a group of
interdependent packages can be distributed and installed as a single unit.
The generated meta-package records the exact archive versions it was built
from and installs its components in dependency order, so that whoever
receives it does not have to work out which package to install first. The
component archives are copied into the generated meta-package, so it is
the only artifact that has to be distributed and no directory has to be
agreed on between machines. Resolves dependencies by building a graph with
topological ordering and cycle detection, classifies them as local or
external, and detects implicit dependencies by scanning source code.
Installation needs no repository access unless a component depends on a
package that only exists in one, which suits teams working behind
institutional firewalls. Generates the complete meta-package scaffold,
including installation helpers, vignettes and documentation.

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
