%global packname  envi
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Environmental Interpolation using Spatial Kernel Density Estimation

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-concaveman 
BuildRequires:    R-CRAN-cvAUC 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sparr 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-concaveman 
Requires:         R-CRAN-cvAUC 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-maptools 
Requires:         R-parallel 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sparr 
Requires:         R-CRAN-spatstat 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimates an ecological niche using occurrence data, covariates, and
kernel density-based estimation methods. For a single species with
presence and absence data, the 'envi' package uses the spatial relative
risk function that is estimated using the 'sparr' package. Details about
the 'sparr' package methods can be found in the tutorial: Davies et al.
(2018) <doi:10.1002/sim.7577>. Details about kernel density estimation can
be found in J. F. Bithell (1990) <doi:10.1002/sim.4780090616>.  More
information about relative risk functions using kernel density estimation
can be found in J. F. Bithell (1991) <doi:10.1002/sim.4780101112>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
