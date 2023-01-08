%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDTSA
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Time Series Analysis Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-clime 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-clime 
Requires:         R-CRAN-sandwich 
Requires:         R-methods 

%description
Procedures for high-dimensional time series analysis including factor
analysis proposed by Lam and Yao (2012) <doi:10.1214/12-AOS970> and Chang,
Guo and Yao (2015) <doi:10.1016/j.jeconom.2015.03.024>, martingale
difference test proposed by Chang, Jiang and Shao (2021) preprint,
principal component analysis proposed by Chang, Guo and Yao (2018)
<doi:10.1214/17-AOS1613>, identifying conintegration proposed by Zhang,
Robinson and Yao (2019) <doi:10.1080/01621459.2018.1458620>, unit root
test proposed by Chang, Cheng and Yao (2021) <doi:10.1093/biomet/asab034>
and white noise test proposed by Chang, Yao and Zhou (2017)
<doi:10.1093/biomet/asw066>.

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
