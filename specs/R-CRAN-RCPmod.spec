%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RCPmod
%global packver   2.192
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.192
Release:          1%{?dist}%{?buildtag}
Summary:          Regions of Common Profiles Modelling with Mixtures-of-Experts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet >= 2.0.13
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-fishMod 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-glmnet >= 2.0.13
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-fishMod 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 

%description
Identifies regions of common (species) profiles (RCPs), possibly when
sampling artefacts are present.  Within a region the probability of
sampling all species remains approximately constant.  This is performed
using mixtures-of-experts models.  The package also contains associated
methods, such as diagnostics. Details of the method can be found in Foster
et al (2013) <doi:10.1002/env.2245> and Foster et al. (2017)
<doi:10.1111/rssc.12211>.

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
