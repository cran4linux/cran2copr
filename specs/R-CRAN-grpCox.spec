%global packname  grpCox
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Cox Model for High-Dimensional Data with Grouped Predictors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix >= 1.2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix >= 1.2.10
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-MASS 
Requires:         R-CRAN-colorspace 

%description
Fit the penalized Cox models with both non-overlapping and overlapping
grouped penalties including the group lasso, group smoothly clipped
absolute deviation, and group minimax concave penalty. The algorithms
combine the MM approach and group-wise descent with some computational
tricks including the screening, active set, and warm-start. Different
tuning regularization parameter methods are provided.

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
