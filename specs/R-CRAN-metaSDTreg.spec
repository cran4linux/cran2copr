%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaSDTreg
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Models for Meta Signal Detection Theory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ordinal >= 2022.11.16
BuildRequires:    R-CRAN-maxLik >= 1.5.2
BuildRequires:    R-CRAN-Matrix >= 1.4.0
BuildRequires:    R-CRAN-truncnorm >= 1.0.8
Requires:         R-CRAN-ordinal >= 2022.11.16
Requires:         R-CRAN-maxLik >= 1.5.2
Requires:         R-CRAN-Matrix >= 1.4.0
Requires:         R-CRAN-truncnorm >= 1.0.8

%description
Regression methods for the meta-SDT model. The package implements methods
for cognitive experiments of metacognition as described in Kristensen, S.
B., Sandberg, K., & Bibby, B. M. (2020). Regression methods for
metacognitive sensitivity. Journal of Mathematical Psychology, 94.
<doi:10.1016/j.jmp.2019.102297>.

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
