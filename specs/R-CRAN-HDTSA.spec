%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDTSA
%global packver   1.0.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5.1
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
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-jointDiag 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-clime 
Requires:         R-CRAN-sandwich 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-jointDiag 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-forecast 

%description
An implementation for high-dimensional time series analysis methods,
including factor model for vector time series proposed by Lam and Yao
(2012) <doi:10.1214/12-AOS970> and Chang, Guo and Yao (2015)
<doi:10.1016/j.jeconom.2015.03.024>, martingale difference test proposed
by Chang, Jiang and Shao (2023) <doi:10.1016/j.jeconom.2022.09.001>,
principal component analysis for vector time series proposed by Chang, Guo
and Yao (2018) <doi:10.1214/17-AOS1613>, cointegration analysis proposed
by Zhang, Robinson and Yao (2019) <doi:10.1080/01621459.2018.1458620>,
unit root test proposed by Chang, Cheng and Yao (2022)
<doi:10.1093/biomet/asab034>, white noise test proposed by Chang, Yao and
Zhou (2017) <doi:10.1093/biomet/asw066>, CP-decomposition for matrix time
series proposed by Chang et al. (2023) <doi:10.1093/jrsssb/qkac011> and
Chang et al. (2024) <doi:10.48550/arXiv.2410.05634>, and statistical
inference for spectral density matrix proposed by Chang et al. (2022)
<doi:10.48550/arXiv.2212.13686>.

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
