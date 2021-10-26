%global __brp_check_rpaths %{nil}
%global packname  PowerUpR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis Tools for Multilevel Randomized Experiments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Includes tools to calculate statistical power, minimum detectable effect
size (MDES), MDES difference (MDESD), and minimum required sample size for
various multilevel randomized experiments (MRE) with continuous outcomes.
Accomodates 14 types of MRE designs to detect main treatment effect, seven
types of MRE designs to detect moderated treatment effect (2-1-1, 2-1-2,
2-2-1, 2-2-2, 3-3-1, 3-3-2, and 3-3-3 designs; <total.lev> - <trt.lev> -
<mod.lev>), five types of MRE designs to detect mediated treatment effects
(2-1-1, 2-2-1, 3-1-1, 3-2-1, and 3-3-1 designs; <trt.lev> - <med.lev> -
<out.lev>), four types of partially nested (PN) design to detect main
treatment effect, and three types of PN designs to detect mediated
treatment effects (2/1, 3/1, 3/2; <trt.arm.lev> / <ctrl.arm.lev>). See
'PowerUp!' Excel series at <https://www.causalevaluation.org/>.

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
