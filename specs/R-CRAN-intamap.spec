%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  intamap
%global packver   1.5-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.11
Release:          1%{?dist}%{?buildtag}
Summary:          Procedures for Automated Interpolation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gstat >= 0.9.36
BuildRequires:    R-CRAN-sp >= 0.9.0
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-gstat >= 0.9.36
Requires:         R-CRAN-sp >= 0.9.0
Requires:         R-CRAN-sf 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 

%description
Geostatistical interpolation has traditionally been done by manually
fitting a variogram and then interpolating. Here, we introduce classes and
methods that can do this interpolation automatically. Pebesma et al (2010)
gives an overview of the methods behind and possible usage
<doi:10.1016/j.cageo.2010.03.019>.

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
