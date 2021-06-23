%global __brp_check_rpaths %{nil}
%global packname  nprobust
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Robust Estimation and Inference Methods usingLocal Polynomial Regression and Kernel Density Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 

%description
Tools for data-driven statistical analysis using local polynomial
regression and kernel density estimation methods as described in Calonico,
Cattaneo and Farrell (2018, <doi:10.1080/01621459.2017.1285776>):
lprobust() for local polynomial point estimation and robust bias-corrected
inference, lpbwselect() for local polynomial bandwidth selection,
kdrobust() for kernel density point estimation and robust bias-corrected
inference, kdbwselect() for kernel density bandwidth selection, and
nprobust.plot() for plotting results. The main methodological and
numerical features of this package are described in Calonico, Cattaneo and
Farrell (2019, <doi:10.18637/jss.v091.i08>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
