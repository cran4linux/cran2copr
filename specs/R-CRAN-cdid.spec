%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cdid
%global packver   1.3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Chained Difference-in-Differences

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-did >= 2.5.1
BuildRequires:    R-CRAN-DRDID >= 1.4.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-parallel 
Requires:         R-CRAN-did >= 2.5.1
Requires:         R-CRAN-DRDID >= 1.4.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-parallel 

%description
Estimates group-time average treatment effects in panels with missing
outcomes by the chained difference-in-differences method of Bellégo,
Benatia and Dortet-Bernadet (2025) <doi:10.1016/j.jeconom.2024.105783>.
The package extends 'did' and retains the att_gt() and aggte() interfaces.
Chained estimation combines observed changes within units by the
generalized method of moments. It supports inverse probability weighting,
outcome regression and doubly robust estimation. Missing outcomes can be
handled by observation weighting, imputation of outcome changes, or an
augmented combination of both. Users can choose comparison groups and
parallel trends assumptions, fit linear cohort-by-date fixed effects, test
trends before treatment, and inspect fitted regression models. A separate
analysis estimates the effects of starting and stopping a binary treatment
under no carryover. Ordinary mode uses the estimators of Callaway and
Sant'Anna (2021) <doi:10.1016/j.jeconom.2020.12.001>.

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
