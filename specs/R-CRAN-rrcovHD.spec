%global __brp_check_rpaths %{nil}
%global packname  rrcovHD
%global packver   0.2-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Multivariate Methods for High Dimensional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rrcov >= 1.3.7
BuildRequires:    R-CRAN-robustbase >= 0.92.1
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-spls 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-robustHD 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-rrcov >= 1.3.7
Requires:         R-CRAN-robustbase >= 0.92.1
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-spls 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-robustHD 
Requires:         R-CRAN-Rcpp 

%description
Robust multivariate methods for high dimensional data including outlier
detection (Filzmoser and Todorov (2013) <doi:10.1016/j.ins.2012.10.017>),
robust sparse PCA (Croux et al. (2013) <doi:10.1080/00401706.2012.727746>,
Todorov and Filzmoser (2013) <doi:10.1007/978-3-642-33042-1_31>), robust
PLS (Todorov and Filzmoser (2014) <doi:10.17713/ajs.v43i4.44>), and robust
sparse classification (Ortner et al. (2020)
<doi:10.1007/s10618-019-00666-8>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
