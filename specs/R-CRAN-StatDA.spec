%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StatDA
%global packver   1.7.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.11
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis for Environmental Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sgeostat 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geoR 
Requires:         R-methods 
Requires:         R-CRAN-sgeostat 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geoR 

%description
Statistical analysis methods for environmental data are implemented. There
is a particular focus on robust methods, and on methods for compositional
data. In addition, larger data sets from geochemistry are provided. The
statistical methods are described in Reimann, Filzmoser, Garrett, Dutter
(2008, ISBN:978-0-470-98581-6).

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
