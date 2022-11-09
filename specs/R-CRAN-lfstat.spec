%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lfstat
%global packver   0.9.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.12
Release:          1%{?dist}%{?buildtag}
Summary:          Calculation of Low Flow Statistics for Daily Stream Flow Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lmom 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-lmomRFA 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lmom 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-lmomRFA 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 

%description
The "Manual on Low-flow Estimation and Prediction" (Gustard & Demuth
(2009, ISBN:978-92-63-11029-9)), published by the World Meteorological
Organisation, gives a comprehensive summary on how to analyse stream flow
data focusing on low-flows. This packages provides functions to compute
the described statistics and produces plots similar to the ones in the
manual.

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
