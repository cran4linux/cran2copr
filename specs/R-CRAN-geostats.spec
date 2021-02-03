%global packname  geostats
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Introduction to Statistics for Geoscientists

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
A collection of datasets and simplified functions for an introductory
(geo)statistics module at University College London. Provides
functionality for compositional, directional and spatial data, including
ternary diagrams, Wulff and Schmidt stereonets, and ordinary kriging
interpolation. Implements logistic and (additive and centred) logratio
transformations. Computes vector averages and concentration parameters for
the von-Mises distribution. Includes a collection of natural and synthetic
fractals, and a simulator for deterministic chaos using a magnetic
pendulum example. The main purpose of these functions is pedagogical.
Researchers can find more complete alternatives for these tools in other
packages such as 'compositions', 'robCompositions', 'sp', 'gstat' and
'RFOC'. All the functions are written in plain R, with no compiled code
and a minimal number of dependencies. Theoretical background and worked
examples are available at <https://tinyurl.com/UCLgeostats/>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
