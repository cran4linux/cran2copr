%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MigConnectivity
%global packver   0.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Migratory Connectivity for Migratory Animals

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RMark >= 2.1.14
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ncf 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-RMark >= 2.1.14
Requires:         R-CRAN-coda 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-gplots 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-ncf 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shape 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 
Requires:         R-CRAN-VGAM 

%description
Allows the user to estimate transition probabilities for migratory animals
between any two phases of the annual cycle, using a variety of different
data types. Also quantifies the strength of migratory connectivity (MC), a
standardized metric to quantify the extent to which populations co-occur
between two phases of the annual cycle. Includes functions to estimate MC
and the more traditional metric of migratory connectivity strength (Mantel
correlation) incorporating uncertainty from multiple sources of sampling
error. For cross-species comparisons, methods are provided to estimate
differences in migratory connectivity strength, incorporating uncertainty.
See Cohen et al. (2018) <doi:10.1111/2041-210X.12916>, Cohen et al. (2019)
<doi:10.1111/ecog.03974>, and Roberts et al. (2023) <doi:10.1002/eap.2788>
for details on some of these methods.

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
