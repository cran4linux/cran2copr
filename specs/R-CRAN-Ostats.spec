%global __brp_check_rpaths %{nil}
%global packname  Ostats
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          O-Stats, or Pairwise Community-Level Niche Overlap Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-hypervolume 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-hypervolume 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-viridis 
Requires:         R-grid 
Requires:         R-CRAN-MASS 

%description
O-statistics, or overlap statistics, measure the degree of community-level
trait overlap. They are estimated by fitting nonparametric kernel density
functions to each species’ trait distribution and calculating their areas
of overlap. For instance, the median pairwise overlap for a community is
calculated by first determining the overlap of each species pair in trait
space, and then taking the median overlap of each species pair in a
community. This median overlap value is called the O-statistic (O for
overlap). The Ostats() function calculates separate univariate overlap
statistics for each trait, while the Ostats_multivariate() function
calculates a single multivariate overlap statistic for all traits.
O-statistics can be evaluated against null models to obtain standardized
effect sizes. 'Ostats' is part of the collaborative Macrosystems
Biodiversity Project "Local- to continental-scale drivers of biodiversity
across the National Ecological Observatory Network (NEON)." For more
information on this project, see the Macrosystems Biodiversity Website
(<https://neon-biodiversity.github.io/>). Calculation of O-statistics is
described in Read et al. (2018) <doi:10.1111/ecog.03641>, and a teaching
module for introducing the underlying biological concepts at an
undergraduate level is described in Grady et al. (2018)
<http://tiee.esa.org/vol/v14/issues/figure_sets/grady/abstract.html>.

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
