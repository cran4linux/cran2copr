%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nutrigon
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Angular Separation Between Nutritional Optima

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-withr 

%description
Fits response surfaces (ordinary least squares, generalized linear models
with any family including quasi-families, or linear mixed-effects models)
to trait data collected under the Geometric Framework for Nutrition and
computes the angular separation (theta) between the nutritional optima of
two traits, with percentile bootstrap confidence intervals that propagate
surface-estimation uncertainty (case or stratified resampling; paired or
unpaired). Provides a design-matched coverage check that simulates
validation configurations on the user's own design and at the
signal-to-noise ratio of the fitted surfaces, an equivalence test for
alignment of optima, local Gaussian and mean curvature, and a surface-area
ratio. Includes the Drosophila lifespan and fecundity dataset of Lee et
al. (2008) "Lifespan and reproduction in Drosophila: new insights from
nutritional geometry" <doi:10.1073/pnas.0710787105> as a worked example.
The angular approach was introduced in Morimoto (2023) "Nutrigonometry I:
using right-angle triangles to quantify nutritional trade-offs in
performance landscapes" <doi:10.1086/723599>.

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
