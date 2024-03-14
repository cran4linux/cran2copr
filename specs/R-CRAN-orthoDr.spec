%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  orthoDr
%global packver   0.6.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.8
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Dimension Reduction Models Using Orthogonality Constrained Optimization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-MASS 

%description
Utilize an orthogonality constrained optimization algorithm of Wen & Yin
(2013) <DOI:10.1007/s10107-012-0584-1> to solve a variety of dimension
reduction problems in the semiparametric framework, such as Ma & Zhu
(2012) <DOI:10.1080/01621459.2011.646925>, Ma & Zhu (2013)
<DOI:10.1214/12-AOS1072>, Sun, Zhu, Wang & Zeng (2019)
<DOI:10.1093/biomet/asy064> and Zhou, Zhu & Zeng (2021)
<DOI:10.1093/biomet/asaa087>. The package also implements some existing
dimension reduction methods such as hMave by Xia, Zhang, & Xu (2010)
<DOI:10.1198/jasa.2009.tm09372> and partial SAVE by Feng, Wen & Zhu (2013)
<DOI:10.1080/01621459.2012.746065>. It also serves as a general purpose
optimization solver for problems with orthogonality constraints, i.e., in
Stiefel manifold. Parallel computing for approximating the gradient is
enabled through 'OpenMP'.

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
