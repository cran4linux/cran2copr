%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rquake
%global packver   2.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Seismic Hypocenter Determination

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
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
Non-linear inversion for hypocenter estimation and analysis of seismic
data collected continuously, or in trigger mode. The functions organize
other functions from 'RSEIS' and 'GEOmap' to help researchers pick,
locate, and store hypocenters for detailed seismic investigation. Error
ellipsoids and station influence are estimated via jackknife analysis.
References include Iversen, E. S., and J. M. Lees
(1996)<doi:10.1785/BSSA0860061853>.

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
