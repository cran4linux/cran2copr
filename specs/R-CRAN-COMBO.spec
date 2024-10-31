%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  COMBO
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Correcting Misclassified Binary Outcomes in Association Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-utils >= 4.2.0
BuildRequires:    R-CRAN-rjags >= 4.13
BuildRequires:    R-CRAN-turboEM >= 2021
BuildRequires:    R-CRAN-tidyr >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-SAMBA >= 0.9.0
BuildRequires:    R-CRAN-Matrix > 1.4.1
Requires:         R-utils >= 4.2.0
Requires:         R-CRAN-rjags >= 4.13
Requires:         R-CRAN-turboEM >= 2021
Requires:         R-CRAN-tidyr >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-SAMBA >= 0.9.0
Requires:         R-CRAN-Matrix > 1.4.1

%description
Use frequentist and Bayesian methods to estimate parameters from a binary
outcome misclassification model. These methods correct for the problem of
"label switching" by assuming that the sum of outcome sensitivity and
specificity is at least 1. A description of the analysis methods is
available in Hochstedler and Wells (2023) <doi:10.48550/arXiv.2303.10215>.

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
