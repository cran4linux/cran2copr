%global __brp_check_rpaths %{nil}
%global packname  stream
%global packver   1.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Infrastructure for Data Stream Mining

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dbscan >= 1.0.0
BuildRequires:    R-CRAN-proxy >= 0.4.7
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-dbscan >= 1.0.0
Requires:         R-CRAN-proxy >= 0.4.7
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-methods 
Requires:         R-CRAN-registry 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-fpc 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mlbench 
Requires:         R-stats 
Requires:         R-utils 

%description
A framework for data stream modeling and associated data mining tasks such
as clustering and classification. The development of this package was
supported in part by NSF IIS-0948893 and NIH R21HG005912. Hahsler et al
(2017) <doi:10.18637/jss.v076.i14>.

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
