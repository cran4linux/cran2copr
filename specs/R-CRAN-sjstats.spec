%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sjstats
%global packver   0.19.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.19.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Convenient Functions for Common Statistical Computations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-effectsize >= 0.8.8
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-datawizard 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-stats 
Requires:         R-CRAN-effectsize >= 0.8.8
Requires:         R-utils 
Requires:         R-CRAN-datawizard 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-performance 
Requires:         R-stats 

%description
Collection of convenient functions for common statistical computations,
which are not directly provided by R's base or stats packages. This
package aims at providing, first, shortcuts for statistical measures,
which otherwise could only be calculated with additional effort (like
Cramer's V, Phi, or effect size statistics like Eta or Omega squared), or
for which currently no functions available. Second, another focus lies on
weighted variants of common statistical measures and tests like weighted
standard error, mean, t-test, correlation, and more.

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
