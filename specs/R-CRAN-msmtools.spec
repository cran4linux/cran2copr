%global packname  msmtools
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Building Augmented Data to Run Multi-State Models with 'msm' Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-survival >= 2.38.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-msm >= 1.6
BuildRequires:    R-CRAN-patchwork >= 1.1.1
BuildRequires:    R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-survival >= 2.38.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-msm >= 1.6
Requires:         R-CRAN-patchwork >= 1.1.1
Requires:         R-CRAN-scales >= 1.1.1

%description
A fast and general method for restructuring classical longitudinal data
into augmented ones. The reason for this is to facilitate the modeling of
longitudinal data under a multi-state framework using the 'msm' package.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
