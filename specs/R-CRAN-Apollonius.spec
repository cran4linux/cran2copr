%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Apollonius
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          2D Apollonius Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gyro >= 1.3.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-colorsGen 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-Polychrome 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppCGAL 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-gyro >= 1.3.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-colorsGen 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-Polychrome 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Computation of the Apollonius diagram of given 2D points and its dual the
Apollonius graph, also known as the additively weighted Voronoï diagram,
and which is a generalization of the classical Voronoï diagram. For
references, see the bibliography in the CGAL documentation at
<https://doc.cgal.org/latest/Apollonius_graph_2/citelist.html>.

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
