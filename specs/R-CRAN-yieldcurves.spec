%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  yieldcurves
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Yield Curve Fitting, Analysis, and Decomposition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-graphics 
Requires:         R-stats 

%description
Fits yield curves using Nelson-Siegel (1987) <doi:10.1086/296409>,
Svensson (1994) <doi:10.3386/w4871>, and cubic spline methods. Extracts
forward rates, discount factors, and par rates from fitted curves.
Computes duration and convexity risk measures. Computes Z-spread and key
rate durations. Provides principal component decomposition following
Litterman and Scheinkman (1991) <doi:10.3905/jfi.1991.692347>, carry and
roll-down analysis, and slope measures. All methods are pure computation
with no external dependencies beyond base R; works with yield data from
any source.

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
