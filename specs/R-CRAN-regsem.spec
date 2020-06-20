%global packname  regsem
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}
Summary:          Regularized Structural Equation Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rsolnp 

%description
Uses both ridge and lasso penalties (and extensions) to penalize specific
parameters in structural equation models. The package offers additional
cost functions, cross validation, and other extensions beyond traditional
structural equation models. Also contains a function to perform
exploratory mediation (XMed).

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

%files
%{rlibdir}/%{packname}
