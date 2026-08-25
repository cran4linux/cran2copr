%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drmeta
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Design-Indexed Location-Scale Meta-Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits constrained and unrestricted meta-analytic location-scale models in
which residual between-study heterogeneity is modeled as an exponential
function of a prespecified design-robustness score. The package supports
maximum-likelihood (ML) and restricted maximum-likelihood (REML)
estimation, location moderators, the conventional random-effects model as
a nested special case, exact estimation at the nonnegative scale-gradient
boundary, design-indexed heterogeneity summaries, scale-attenuation
measures, prediction of fitted heterogeneity, leave-one-out influence
diagnostics, and parametric-bootstrap inference for the scale gradient.
Because the scale-gradient null lies on the boundary of the constrained
parameter space, standard chi-square likelihood-ratio references do not
apply (Self and Liang, 1987, <doi:10.1080/01621459.1987.10478472>). The
general location-scale parent model is described in Viechtbauer and
Lopez-Lopez (2022, <doi:10.1002/jrsm.1562>). A scale model reweights
studies and does not adjust the mean for design-linked bias.

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
