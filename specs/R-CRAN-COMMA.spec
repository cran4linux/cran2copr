%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  COMMA
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Correcting Misclassified Mediation Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.3.1
BuildRequires:    R-CRAN-turboEM >= 2021
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-Matrix > 1.4.1
Requires:         R-parallel >= 4.3.1
Requires:         R-CRAN-turboEM >= 2021
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-Matrix > 1.4.1

%description
Use three methods to estimate parameters from a mediation analysis with a
binary misclassified mediator. These methods correct for the problem of
"label switching" using Youden's J criteria. A detailed description of the
analysis methods is available in Webb and Wells (2024), "Effect estimation
in the presence of a misclassified binary mediator"
<doi:10.48550/arXiv.2407.06970>.

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
