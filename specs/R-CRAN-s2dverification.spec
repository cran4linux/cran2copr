%global __brp_check_rpaths %{nil}
%global packname  s2dverification
%global packver   2.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          Set of Common Tools for Forecast Verification

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-SpecsVerification >= 0.5.0
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-GEOmap 
BuildRequires:    R-CRAN-geomapdata 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-SpecsVerification >= 0.5.0
Requires:         R-CRAN-maps 
Requires:         R-methods 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-GEOmap 
Requires:         R-CRAN-geomapdata 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-ncdf4 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 

%description
Set of tools to verify forecasts through the computation of typical
prediction scores against one or more observational datasets or reanalyses
(a reanalysis being a physical extrapolation of observations that relies
on the equations from a model, not a pure observational dataset). Intended
for seasonal to decadal climate forecasts although can be useful to verify
other kinds of forecasts. The package can be helpful in climate sciences
for other purposes than forecasting. To find more details, see the review
paper Manubens, N.et al. (2018) <doi:10.1016/j.envsoft.2018.01.018>.

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
