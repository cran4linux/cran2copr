%global packname  springer
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Sparse Group Variable Selection for Gene-EnvironmentInteractions in the Longitudinal Study

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 

%description
Recently, regularized variable selection has emerged as a powerful tool to
identify and dissect gene-environment interactions. Nevertheless, in
longitudinal studies with high dimensional genetic factors, regularization
methods for G×E interactions have not been systematically developed. In
this package, we provide the implementation of sparse group variable
selection, based on both the quadratic inference function (QIF) and
generalized estimating equation (GEE), to accommodate the bi-level
selection for longitudinal G×E studies with high dimensional genomic
features. Alternative methods conducting only the group or individual
level selection have also been included. The core modules of the package
have been developed in C++.

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
