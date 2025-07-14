%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bSims
%global packver   0.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Agent-Based Bird Point Count Simulator

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-deldir >= 1.0.2
BuildRequires:    R-CRAN-intrval 
BuildRequires:    R-CRAN-mefa4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-deldir >= 1.0.2
Requires:         R-CRAN-intrval 
Requires:         R-CRAN-mefa4 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 

%description
A highly scientific and utterly addictive bird point count simulator to
test statistical assumptions, aid survey design, and have fun while doing
it (Solymos 2024 <doi:10.1007/s42977-023-00183-2>). The simulations follow
time-removal and distance sampling models based on Matsuoka et al. (2012)
<doi:10.1525/auk.2012.11190>, Solymos et al. (2013)
<doi:10.1111/2041-210X.12106>, and Solymos et al. (2018)
<doi:10.1650/CONDOR-18-32.1>, and sound attenuation experiments by Yip et
al. (2017) <doi:10.1650/CONDOR-16-93.1>.

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
