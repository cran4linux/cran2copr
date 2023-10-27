%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimEngine
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Modular Framework for Statistical Simulations in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.2.2
BuildRequires:    R-methods >= 4.2.2
BuildRequires:    R-utils >= 4.2.2
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-pbapply >= 1.6.0
BuildRequires:    R-CRAN-data.table >= 1.14.6
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-dplyr >= 1.0.10
Requires:         R-parallel >= 4.2.2
Requires:         R-methods >= 4.2.2
Requires:         R-utils >= 4.2.2
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-pbapply >= 1.6.0
Requires:         R-CRAN-data.table >= 1.14.6
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-dplyr >= 1.0.10

%description
An open-source R package for structuring, maintaining, running, and
debugging statistical simulations on both local and cluster-based
computing environments.See full documentation at
<https://avi-kenny.github.io/SimEngine/>.

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
