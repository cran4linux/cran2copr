%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  viewscape
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Viewscape Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-ForestTools >= 1.0.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbmcapply 
Requires:         R-CRAN-ForestTools >= 1.0.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-terra 
Requires:         R-parallel 
Requires:         R-CRAN-pbmcapply 

%description
A collection of functions to make R a more effective viewscape analysis
tool for calculating viewscape metrics based on computing the viewable
area for given a point/multiple viewpoints and a digital elevation
model.The method of calculating viewscape metrics implemented in this
package are based on the work of Tabrizian et al. (2020)
<doi:10.1016/j.landurbplan.2019.103704>. The algorithm of computing
viewshed is based on the work of Franklin & Ray. (1994)
<https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=555780f6f5d7e537eb1edb28862c86d1519af2be>.

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
