%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  transfR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transfer of Hydrograph from Gauged to Ungauged Catchments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sf >= 0.8.0
BuildRequires:    R-CRAN-stars >= 0.4.0
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-sf >= 0.8.0
Requires:         R-CRAN-stars >= 0.4.0
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-units 
Requires:         R-CRAN-Rdpack 

%description
A geomorphology-based hydrological modelling for transferring streamflow
measurements from gauged to ungauged catchments. Inverse modelling enables
to estimate net rainfall from streamflow measurements following Boudhraâ
et al. (2018) <doi:10.1080/02626667.2018.1425801>. Resulting net rainfall
is then estimated on the ungauged catchments by spatial interpolation in
order to finally simulate streamflow following de Lavenne et al. (2016)
<doi:10.1002/2016WR018716>.

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
