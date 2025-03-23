%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RPhosFate
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Soil and Chemical Substance Emission and Transport Model

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-checkmate 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
An enhanced version of the semi-empirical, spatially distributed emission
and transport model PhosFate implemented in 'R' and 'C++'. It is based on
the D-infinity, but also supports the D8 flow method. The currently
available substances are suspended solids (SS) and particulate phosphorus
(PP). A major feature is the allocation of substance loads entering
surface waters to their sources of origin, which is a basic requirement
for the identification of critical source areas and in consequence a
cost-effective implementation of mitigation measures. References: Hepp et
al. (2022) <doi:10.1016/j.jenvman.2022.114514>; Hepp and Zessner (2019)
<doi:10.3390/w11102161>; Kovacs (2013)
<http://hdl.handle.net/20.500.12708/9468>.

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
