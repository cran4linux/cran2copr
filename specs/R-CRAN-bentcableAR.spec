%global __brp_check_rpaths %{nil}
%global packname  bentcableAR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bent-Cable Regression for Independent Data or Autoregressive Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Included are two main interfaces, bentcable.ar() and bentcable.dev.plot(),
for fitting and diagnosing bent-cable regressions for autoregressive
time-series data (Chiu and Lockhart 2010, <doi:10.1002/cjs.10070>) or
independent data (time series or otherwise - Chiu, Lockhart and Routledge
2006, <doi:10.1198/016214505000001177>). Some components in the package
can also be used as stand-alone functions. The bent cable
(linear-quadratic-linear) generalizes the broken stick (linear-linear),
which is also handled by this package. Version 0.2 corrected a glitch in
the computation of confidence intervals for the CTP. References that were
updated from Versions 0.2.1 and 0.2.2 appear in Version 0.2.3 and up.
Version 0.3.0 improved robustness of the error-message producing
mechanism. Version 0.3.1 improves the NAMESPACE file of the package. It is
the author's intention to distribute any future updates via GitHub.

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
