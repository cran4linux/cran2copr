%global __brp_check_rpaths %{nil}
%global packname  rare
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Model with Tree-Based Lasso Regularization for Rare Features

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Rcpp 

%description
Implementation of an alternating direction method of multipliers algorithm
for fitting a linear model with tree-based lasso regularization, which is
proposed in Algorithm 1 of Yan and Bien (2018) <arXiv:1803.06675>. The
package allows efficient model fitting on the entire 2-dimensional
regularization path for large datasets. The complete set of functions also
makes the entire process of tuning regularization parameters and
visualizing results hassle-free.

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
