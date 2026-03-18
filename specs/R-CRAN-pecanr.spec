%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pecanr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Eta-Squared for Crossed and Nested Linear Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-lme4 

%description
Computes partial eta-squared effect sizes for fixed effects in linear
mixed models fitted with the 'lme4' package. Supports crossed and nested
random effects structures with any number of grouping factors. Random
slope variances are translated to the outcome scale using a variance
decomposition approach, correctly accounting for predictor scaling and
interaction terms. Both general and operative effect sizes are provided.
Methods are based on Correll, Mellinger, McClelland, and Judd (2020)
<doi:10.1016/j.tics.2019.12.009>, Correll, Mellinger, and Pedersen (2022)
<doi:10.3758/s13428-021-01687-2>, and Rights and Sterba (2019)
<doi:10.1037/met0000184>.

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
