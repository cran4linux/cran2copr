%global packname  Rforestry
%global packver   0.9.0.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0.40
Release:          1%{?dist}%{?buildtag}
Summary:          Random Forests, Linear Trees, and Gradient Boosting for Inference and Interpretability

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-onehot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-glmnet 
Requires:         R-grDevices 
Requires:         R-CRAN-onehot 
Requires:         R-CRAN-dplyr 

%description
Provides fast implementations of Honest Random Forests, Gradient Boosting,
and Linear Random Forests, with an emphasis on inference and
interpretability. Additionally contains methods for variable importance,
out-of-bag prediction, regression monotonicity, and several methods for
missing data imputation. Soren R. Kunzel, Theo F. Saarinen, Edward W. Liu,
Jasjeet S. Sekhon (2019) <arXiv:1906.06463>.

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
