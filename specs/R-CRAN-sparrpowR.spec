%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparrpowR
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis to Detect Spatial Relative Risk Clusters

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-sparr 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-sparr 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
Calculate the statistical power to detect clusters using kernel-based
spatial relative risk functions that are estimated using the 'sparr'
package. Details about the 'sparr' package methods can be found in the
tutorial: Davies et al. (2018) <doi:10.1002/sim.7577>. Details about
kernel density estimation can be found in J. F. Bithell (1990)
<doi:10.1002/sim.4780090616>. More information about relative risk
functions using kernel density estimation can be found in J. F. Bithell
(1991) <doi:10.1002/sim.4780101112>.

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
