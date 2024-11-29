%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HTSeedGLM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hydro Thermal Time Analysis of Seed Germination Using Generalised Linear Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Seed germinates through the physical process of water uptake by dry seed
driven by the difference in water potential between the seed and the
water. There exists seed-to-seed variability in the base seed water
potential. Hence, there is a need for a distribution such that a viable
seed with its base seed water potential germinates if and only if the soil
water potential is more than the base seed water potential. This package
estimates the stress tolerance and uniformity parameters of the seed lot
for germination under various temperatures by using the hydro-time model
of counts of germinated seeds under various water potentials. The
distribution of base seed water potential has been considered to follow
Normal, Logistic and Extreme value distribution. The estimated proportion
of germinated seeds along with the estimates of stress and uniformity
parameters are obtained using a generalised linear model. The significance
test of the above parameters for within and between temperatures is also
performed in the analysis. Details can be found in Kebreab and Murdoch
(1999) <doi:10.1093/jxb/50.334.655> and Bradford (2002)
<https://www.jstor.org/stable/4046371>.

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
