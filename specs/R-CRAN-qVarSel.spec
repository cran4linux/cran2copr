%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qVarSel
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Select Variables for Optimal Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-lpSolveAPI 

%description
Finding hidden clusters in structured data can be hindered by the presence
of masking variables. If not detected, masking variables are used to
calculate the overall similarities between units, and therefore the
cluster attribution is more imprecise. The algorithm q-vars implements an
optimization method to find the variables that most separate units between
clusters. In this way, masking variables can be discarded from the data
frame and the clustering is more accurate. Tests can be found in Benati et
al.(2017) <doi:10.1080/01605682.2017.1398206>.

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
