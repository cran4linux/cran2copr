%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NTSS
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Tests in Spatial Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.model 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-GET 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.model 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-GET 

%description
Nonparametric test of independence between a pair of spatial objects
(random fields, point processes) based on random shifts with torus or
variance correction. See Mrkvička et al. (2021)
<doi:10.1016/j.spasta.2020.100430>, Dvořák et al. (2022)
<doi:10.1111/insr.12503>, Dvořák and Mrkvička (2022) <arxiv:2210.05424>.

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
