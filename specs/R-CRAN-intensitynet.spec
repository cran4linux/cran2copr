%global __brp_check_rpaths %{nil}
%global packname  intensitynet
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intensity Analysis of Spatial Point Patterns on Complex Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.6.3
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-sna >= 2.6
BuildRequires:    R-CRAN-spatstat.geom >= 2.3.1
BuildRequires:    R-CRAN-intergraph >= 2.0.2
BuildRequires:    R-CRAN-igraph >= 1.2.5
BuildRequires:    R-CRAN-Matrix >= 1.2.18
BuildRequires:    R-CRAN-spdep >= 1.2.1
BuildRequires:    R-CRAN-viridis >= 0.5.1
Requires:         R-methods >= 3.6.3
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-sna >= 2.6
Requires:         R-CRAN-spatstat.geom >= 2.3.1
Requires:         R-CRAN-intergraph >= 2.0.2
Requires:         R-CRAN-igraph >= 1.2.5
Requires:         R-CRAN-Matrix >= 1.2.18
Requires:         R-CRAN-spdep >= 1.2.1
Requires:         R-CRAN-viridis >= 0.5.1

%description
Tools to analyze point patterns in space occurring over planar network
structures derived from graph-related intensity measures for undirected,
directed, and mixed networks. This package is based on the following
research: Eckardt and Mateu (2018) <doi:10.1080/10618600.2017.1391695>.
Eckardt and Mateu (2021) <doi:10.1007/s11749-020-00720-4>.

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
