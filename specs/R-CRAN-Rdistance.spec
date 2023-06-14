%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rdistance
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distance-Sampling Analyses for Density and Abundance Estimation

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-crayon 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-units 
Requires:         R-CRAN-crayon 

%description
Distance-sampling analyses estimate density and abundance of organisms in
ecology when detection probability declines with increasing distance from
the observers. Distance-sampling is popular in most branches of ecology
and especially when organisms are observed from aerial platforms (e.g.,
airplane or drone), surface vessels (e.g., boat or truck), or along
walking transects. Rdistance analyzes data collected on both point and
line transects, estimates overall (study area) and site-level (transect or
point) density, and allows users to specify regression-like formula
(similar to lm or glm) for covariates. A large suite of classical,
parametric detection functions are included along with some uncommon
parametric functions (e.g., Gamma, negative exponential) and
non-parametric smoothed distance functions. Custom (user-defined)
detection functions can be implemented (see vignette).  Measurement unit
integrity is enforced with internal unit conversion when necessary. The
help files and vignettes have been vetted by multiple authors and tested
in workshop settings.

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
