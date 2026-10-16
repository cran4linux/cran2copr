%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EmiStatR
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          A Simplified and Scalable Urban Water Quality Model for Simulation of Combined Sewer Overflows

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-doParallel 

%description
Provides a fast and parallelised calculator to estimate combined sewage
water emissions. It supports the planning and design of urban drainage
systems without extensive simulation tools. The methods are described in
Torres-Matallana et al. (2018) <doi:10.3390/w10060782>.

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
