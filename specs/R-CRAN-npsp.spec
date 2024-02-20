%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npsp
%global packver   0.7-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.13
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Spatial Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-spam 
Requires:         R-graphics 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-spam 

%description
Multidimensional nonparametric spatial (spatio-temporal) geostatistics. S3
classes and methods for multidimensional: linear binning, local polynomial
kernel regression (spatial trend estimation), density and variogram
estimation. Nonparametric methods for simultaneous inference on both
spatial trend and variogram functions (for spatial processes).
Nonparametric residual kriging (spatial prediction). For details on these
methods see, for example, Fernandez-Casal and Francisco-Fernandez (2014)
<doi:10.1007/s00477-013-0817-8> or Castillo-Paez et al. (2019)
<doi:10.1016/j.csda.2019.01.017>.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
