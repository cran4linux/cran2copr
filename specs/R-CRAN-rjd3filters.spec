%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rjd3filters
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Trend-Cycle Extraction with Linear Filters with 'JDemetra+ 3.x'

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjd3toolkit >= 3.7.1
BuildRequires:    R-CRAN-rJava >= 1.0.6
BuildRequires:    R-CRAN-rjd3jars >= 0.0.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rjd3toolkit >= 3.7.1
Requires:         R-CRAN-rJava >= 1.0.6
Requires:         R-CRAN-rjd3jars >= 0.0.5
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Build and apply symmetric and asymmetric moving averages (= linear
filters) for trend-cycle extraction. In particular, it implements several
modern approaches for real-time estimates from the viewpoint of revisions
and time delay in detecting turning points. It includes the local
polynomial approach of Proietti and Luati (2008), the Reproducing Kernel
Hilbert Space (RKHS) of Dagum and Bianconcini (2008) and the
Fidelity-Smoothness-Timeliness approach of Grun-Rehomme, Guggemos, and
Ladiray (2018). It is based on 'Java' libraries developed in 'JDemetra+'
(<https://github.com/jdemetra>), time series analysis software.

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
