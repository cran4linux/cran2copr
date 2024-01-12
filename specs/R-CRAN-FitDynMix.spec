%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FitDynMix
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Dynamic Mixtures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-evir 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-evir 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rdpack 
Requires:         R-parallel 
Requires:         R-CRAN-ks 
Requires:         R-stats 
Requires:         R-graphics 

%description
Estimation of a dynamic lognormal - Generalized Pareto mixture via the
Approximate Maximum Likelihood and the Cross-Entropy methods. See Bee, M.
(2023) <doi:10.1016/j.csda.2023.107764>.

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
