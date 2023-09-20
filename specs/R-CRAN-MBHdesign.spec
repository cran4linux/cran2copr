%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MBHdesign
%global packver   2.3.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.14
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Designs for Ecological and Environmental Surveys

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-class 
Requires:         R-parallel 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-terra 

%description
Provides spatially survey balanced designs using the quasi-random number
method described Robinson et al. (2013) <doi:10.1111/biom.12059> and
adjusted in Robinson et al. (2017) <doi:10.1016/j.spl.2017.05.004>.
Designs using MBHdesign can: 1) accommodate, without substantial
detrimental effects on spatial balance, legacy sites (Foster et al., 2017
<doi:10.1111/2041-210X.12782>); 2) be based on points or transects (foster
et al. 2020 <doi:10.1111/2041-210X.13321> and produce clustered samples
(Foster et al. (in press). Additional information about the package use
itself is given in Foster (2021) <doi:10.1111/2041-210X.13535>.

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
