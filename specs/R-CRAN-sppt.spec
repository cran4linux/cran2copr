%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sppt
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Point Pattern Test for Areal Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-ggspatial 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Implements the area-based nonparametric spatial point pattern test of
Andresen (2009) <doi:10.1016/j.apgeog.2008.12.004> for comparing two
spatial distributions of events aggregated to areal units, with the
applications and extensions reviewed in Andresen (2016)
<doi:10.1177/2059799116630659>. Unit-level inference uses bounded Monte
Carlo bootstrap p-values, with marginal confidence interval overlap
retained as an option. Global similarity is summarised by the robust S
index, accompanied by a test of whether two patterns are more different
than two realisations of a single process, and a test of the spatial
arrangement of the differences. A longitudinal extension compares each
period of a time series against a base period and classifies unit-level
trajectories. Publication-ready maps can be redrawn with user-chosen
layouts.

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
