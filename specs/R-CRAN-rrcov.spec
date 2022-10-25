%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rrcov
%global packver   1.7-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable Robust Estimators with High Breakdown Point

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-robustbase >= 0.92.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-pcaPP 
Requires:         R-CRAN-robustbase >= 0.92.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-pcaPP 

%description
Robust Location and Scatter Estimation and Robust Multivariate Analysis
with High Breakdown Point: principal component analysis (Filzmoser and
Todorov (2013), <doi:10.1016/j.ins.2012.10.017>), linear and quadratic
discriminant analysis (Todorov and Pires (2007)), multivariate tests
(Todorov and Filzmoser (2010) <doi:10.1016/j.csda.2009.08.015>), outlier
detection (Todorov et al. (2010) <doi:10.1007/s11634-010-0075-2>). See
also Todorov and Filzmoser (2009) <ISBN-13:978-3838108148>, Todorov and
Filzmoser (2010) <doi:10.18637/jss.v032.i03> and Boudt et al. (2019)
<doi:10.1007/s11222-019-09869-x>.

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
