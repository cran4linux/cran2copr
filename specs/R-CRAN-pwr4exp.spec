%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pwr4exp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis for Research Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lmerTest >= 3.1.3
BuildRequires:    R-CRAN-car >= 3.1.2
BuildRequires:    R-CRAN-emmeans >= 1.10.3
BuildRequires:    R-CRAN-lme4 >= 1.1.35.4
BuildRequires:    R-methods 
Requires:         R-CRAN-lmerTest >= 3.1.3
Requires:         R-CRAN-car >= 3.1.2
Requires:         R-CRAN-emmeans >= 1.10.3
Requires:         R-CRAN-lme4 >= 1.1.35.4
Requires:         R-methods 

%description
Provides tools for calculating statistical power and determining sample
size for a variety of experimental designs used in agricultural and
biological research, including completely randomized, block, and
split-plot designs. Supports customized designs and allows specification
of main effects, interactions, and contrasts for accurate power analysis.

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
