%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IDF
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Plotting of IDF Curves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-fastmatch 
Requires:         R-stats 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-fastmatch 

%description
Intensity-duration-frequency (IDF) curves are a widely used analysis-tool
in hydrology to assess extreme values of precipitation [e.g. Mailhot et
al., 2007, <doi:10.1016/j.jhydrol.2007.09.019>]. The package 'IDF'
provides functions to estimate IDF parameters for given precipitation time
series on the basis of a duration-dependent generalized extreme value
distribution [Koutsoyiannis et al., 1998,
<doi:10.1016/S0022-1694(98)00097-3>].

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
