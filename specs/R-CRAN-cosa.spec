%global __brp_check_rpaths %{nil}
%global packname  cosa
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bound Constrained Optimal Sample Size Allocation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-msm >= 1.6.7
BuildRequires:    R-CRAN-nloptr >= 1.0.4
Requires:         R-CRAN-msm >= 1.6.7
Requires:         R-CRAN-nloptr >= 1.0.4

%description
Implements bound constrained optimal sample size allocation (BCOSSA)
framework described in Bulus & Dong (2021)
<doi:10.1080/00220973.2019.1636197> for power analysis of multilevel
regression discontinuity designs (MRDDs) and multilevel randomized trials
(MRTs) with continuous outcomes. Minimum detectable effect size (MDES) and
power computations for MRDDs allow polynomial functional form
specification for the score variable (with or without interaction with the
treatment indicator). See Bulus (2021)
<doi:10.1080/19345747.2021.1947425>.

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
