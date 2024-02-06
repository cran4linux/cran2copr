%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spqdep
%global packver   0.1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Testing for Spatial Independence of Qualitative Data in Cross Section

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.8.2
BuildRequires:    R-methods >= 3.5
BuildRequires:    R-stats >= 3.5
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-sp >= 1.4.5
BuildRequires:    R-CRAN-igraph >= 1.2.5
BuildRequires:    R-CRAN-Matrix >= 1.2.18
BuildRequires:    R-CRAN-spatialreg >= 1.1.8
BuildRequires:    R-CRAN-spdep >= 1.1.3
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-broom >= 0.7.2
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-lwgeom >= 0.2.8
BuildRequires:    R-CRAN-gt >= 0.2.2
BuildRequires:    R-CRAN-rgeoda >= 0.0.8.6
BuildRequires:    R-CRAN-rsample >= 0.0.8
Requires:         R-CRAN-gtools >= 3.8.2
Requires:         R-methods >= 3.5
Requires:         R-stats >= 3.5
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-sp >= 1.4.5
Requires:         R-CRAN-igraph >= 1.2.5
Requires:         R-CRAN-Matrix >= 1.2.18
Requires:         R-CRAN-spatialreg >= 1.1.8
Requires:         R-CRAN-spdep >= 1.1.3
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-broom >= 0.7.2
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-lwgeom >= 0.2.8
Requires:         R-CRAN-gt >= 0.2.2
Requires:         R-CRAN-rgeoda >= 0.0.8.6
Requires:         R-CRAN-rsample >= 0.0.8

%description
Testing for Spatial Dependence of Qualitative Data in Cross Section. The
list of functions includes join-count tests, Q test, spatial scan test,
similarity test and spatial runs test. The methodology of these models can
be found in <doi:10.1007/s10109-009-0100-1> and
<doi:10.1080/13658816.2011.586327>.

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
