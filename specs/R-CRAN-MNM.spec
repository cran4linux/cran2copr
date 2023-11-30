%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MNM
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Nonparametric Methods. An Approach Based on Spatial Signs and Ranks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.2
Requires:         R-core >= 2.9.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-SpatialNP 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-ICS 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-SpatialNP 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-ICS 

%description
Multivariate tests, estimates and methods based on the identity score,
spatial sign score and spatial rank score are provided. The methods
include one and c-sample problems, shape estimation and testing, linear
regression and principal components. The methodology is described in Oja
(2010) <doi:10.1007/978-1-4419-0468-3> and Nordhausen and Oja (2011)
<doi:10.18637/jss.v043.i05>.

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
