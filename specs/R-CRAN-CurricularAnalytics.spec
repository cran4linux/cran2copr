%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CurricularAnalytics
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploring and Analyzing Academic Curricula

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.4.0
BuildRequires:    R-tools >= 4.4.0
BuildRequires:    R-utils >= 4.4.0
BuildRequires:    R-CRAN-visNetwork >= 2.1.2
BuildRequires:    R-CRAN-igraph >= 2.0.3
BuildRequires:    R-CRAN-dplyr >= 1.1.4
Requires:         R-stats >= 4.4.0
Requires:         R-tools >= 4.4.0
Requires:         R-utils >= 4.4.0
Requires:         R-CRAN-visNetwork >= 2.1.2
Requires:         R-CRAN-igraph >= 2.0.3
Requires:         R-CRAN-dplyr >= 1.1.4

%description
Provides an implementation of ‘Curricular Analytics’, a framework for
analyzing and quantifying the complexity of academic curricula. Curricula
are modelled as directed acyclic graphs and analytics are provided based
on path lengths and edge density. This work directly comes from Heileman
et al. (2018) <doi:10.48550/arXiv.1811.09676>.

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
