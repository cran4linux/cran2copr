%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  levelSets
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Ray-Based Mapping and Visualization of Level Sets (Excursion Sets)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-withr 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-withr 

%description
An (upper) level set of a function is the set of inputs for which the
function value is at or above a specified threshold.  (Also called an
excursion set).  Applications of level sets include confidence or credible
regions for parameters of statistical models, where the function is the
likelihood or posterior density; regions where classification rules assign
high probability to a given class; and scientific or engineering models
where one is interested in input regions for which model output is above a
threshold.  This package maps out the boundary of a level set by finding
its intersections with collections of 1-dimensional rays, generalizing a
proposal by Kim and Lindsay (Statistica Sinica 21:923-948, 2011).  Tools
are provided to generate rays, find intersections, and visualize results.
The package makes few assumptions about the studied function: it may be
discontinuous, it may have a complicated feasible region, and the target
level set may be non-convex or have multiple, disconnected parts.
Vignettes describe package usage and show examples with two to five input
space dimensions.

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
