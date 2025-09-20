%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clarify
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Inference for Regression Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-pbapply >= 1.7.4
BuildRequires:    R-CRAN-insight >= 1.4.2
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-marginaleffects >= 0.30.0
BuildRequires:    R-CRAN-chk >= 0.10.0
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-pbapply >= 1.7.4
Requires:         R-CRAN-insight >= 1.4.2
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-marginaleffects >= 0.30.0
Requires:         R-CRAN-chk >= 0.10.0

%description
Performs simulation-based inference as an alternative to the delta method
for obtaining valid confidence intervals and p-values for regression
post-estimation quantities, such as average marginal effects and
predictions at representative values. This framework for simulation-based
inference is especially useful when the resulting quantity is not normally
distributed and the delta method approximation fails. The methodology is
described in Greifer, et al. (2025) <doi:10.32614/RJ-2024-015>. 'clarify'
is meant to replace some of the functionality of the archived package
'Zelig'; see the vignette "Translating Zelig to clarify" for replicating
this functionality.

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
