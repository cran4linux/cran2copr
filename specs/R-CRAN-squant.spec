%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  squant
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Subgroup Identification Based on Quantitative Objectives

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-graphics >= 3.4.3
BuildRequires:    R-utils >= 3.4.3
BuildRequires:    R-methods >= 3.4.3
BuildRequires:    R-CRAN-survival >= 2.41.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-glmnet >= 2.0.13
Requires:         R-stats >= 3.4.3
Requires:         R-graphics >= 3.4.3
Requires:         R-utils >= 3.4.3
Requires:         R-methods >= 3.4.3
Requires:         R-CRAN-survival >= 2.41.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-glmnet >= 2.0.13

%description
A subgroup identification method for precision medicine based on
quantitative objectives. This method can handle continuous, binary and
survival endpoint for both prognostic and predictive case. For the
predictive case, the method aims at identifying a subgroup for which
treatment is better than control by at least a pre-specified or
auto-selected constant. For the prognostic case, the method aims at
identifying a subgroup that is at least better than a
pre-specified/auto-selected constant. The derived signature is a linear
combination of predictors, and the selected subgroup are subjects with the
signature > 0. The false discover rate when no true subgroup exists is
controlled at a user-specified level.

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
