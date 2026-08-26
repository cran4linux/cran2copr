%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  interSAE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intersectional Small Area Estimation from Survey and Census Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements design-aware, margin-constrained estimation of population
indicators for geographic areas crossed with demographic subgroups.
Complex-survey microdata supply outcomes and association information,
while one or more aggregate census tables supply overlapping population
margins. A generalized iterative proportional fitting engine reconstructs
a coherent latent population table, and an augmented model-assisted
estimator produces domain means, proportions, and totals for sampled and
unsampled intersections. Tools diagnose non-identification, compute
linear-programming sensitivity bounds, propagate sampling and model
uncertainty with replicate-weight or multiplier bootstrap procedures,
enforce structural zeros, and benchmark estimates to official totals. The
framework extends calibration ideas from Deville and Sarndal (1992)
<doi:10.1080/01621459.1992.10475217> and small area estimation ideas from
Fay and Herriot (1979) <doi:10.1080/01621459.1979.10482505>.

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
