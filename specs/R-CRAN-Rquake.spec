%global __brp_check_rpaths %{nil}
%global packname  Rquake
%global packver   2.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Seismic Hypocenter Determination

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch
BuildRequires:    R-CRAN-RPMG 
BuildRequires:    R-CRAN-RSEIS 
BuildRequires:    R-CRAN-GEOmap 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-minpack.lm 
Requires:         R-CRAN-RPMG 
Requires:         R-CRAN-RSEIS 
Requires:         R-CRAN-GEOmap 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-minpack.lm 

%description
Hypocenter estimation and analysis of seismic data collected continuously,
or in trigger mode. The functions organize other functions from RSEIS and
GEOmap to help researchers pick, locate, and store hypocenters for
detailed seismic investigation.

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
