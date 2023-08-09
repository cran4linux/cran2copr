%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ShapeSelectForest
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Shape Selection for Landsat Time Series of Forest Dynamics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.3.40
BuildRequires:    R-CRAN-coneproj >= 1.6
Requires:         R-CRAN-raster >= 2.3.40
Requires:         R-CRAN-coneproj >= 1.6

%description
Landsat satellites collect important data about global forest conditions.
Documentation about Landsat's role in forest disturbance estimation is
available at the site <https://landsat.gsfc.nasa.gov/>. By constrained
quadratic B-splines, this package delivers an optimal shape-restricted
trajectory to a time series of Landsat imagery for the purpose of modeling
annual forest disturbance dynamics to behave in an ecologically sensible
manner assuming one of seven possible "shapes", namely, flat, decreasing,
one-jump (decreasing, jump up, decreasing), inverted vee (increasing then
decreasing), vee (decreasing then increasing), linear increasing, and
double-jump (decreasing, jump up, decreasing, jump up, decreasing). The
main routine selects the best shape according to the minimum Bayes
information criterion (BIC) or the cone information criterion (CIC), which
is defined as the log of the estimated predictive squared error. The
package also provides parameters summarizing the temporal pattern
including year(s) of inflection, magnitude of change, pre- and
post-inflection rates of growth or recovery. In addition, it contains
routines for converting a flat map of disturbance agents to time-series
disturbance maps and a graphical routine displaying the fitted trajectory
of Landsat imagery.

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
