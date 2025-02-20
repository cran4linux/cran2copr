%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DBCVindex
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates the Density-Based Clustering Validation (DBCV) Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qpdf 
Requires:         R-CRAN-qpdf 

%description
A metric called 'Density-Based Clustering Validation index' (DBCV) index
to evaluate clustering results, following the
<https://github.com/pajaskowiak/clusterConfusion/blob/main/R/dbcv.R> 'R'
implementation by Pablo Andretta Jaskowiak. Original 'DBCV' index article:
Moulavi, D., Jaskowiak, P. A., Campello, R. J., Zimek, A., and Sander, J.
(April 2014), "Density-based clustering validation", Proceedings of SDM
2014 -- the 2014 SIAM International Conference on Data Mining (pp.
839-847), <doi:10.1137/1.9781611973440.96>.

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
