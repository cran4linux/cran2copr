%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatialPack
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Assessment the Association Between Two Spatial Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-fastmatrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-fastmatrix 
Requires:         R-stats 
Requires:         R-graphics 

%description
Tools to assess the association between two spatial processes. Currently,
several methodologies are implemented: A modified t-test to perform
hypothesis testing about the independence between the processes, a
suitable nonparametric correlation coefficient, the codispersion
coefficient, and an F test for assessing the multiple correlation between
one spatial process and several others. Functions for image processing and
computing the spatial association between images are also provided.
Functions contained in the package are intended to accompany Vallejos, R.,
Osorio, F., Bevilacqua, M. (2020). Spatial Relationships Between Two
Georeferenced Variables: With Applications in R. Springer, Cham
<doi:10.1007/978-3-030-56681-4>.

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
