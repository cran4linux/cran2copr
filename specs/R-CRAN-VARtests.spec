%global packname  VARtests
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          Tests for Error Autocorrelation, ARCH Errors, and Cointegrationin Vector Autoregressive Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-sn 

%description
Implements the Wild bootstrap tests for autocorrelation in vector
autoregressive models of Ahlgren, N. & Catani, P. (2016,
<doi:10.1007/s00362-016-0744-0>), the Combined LM test for ARCH in VAR
models of Catani, P. & Ahlgren, N. (2016,
<doi:10.1016/j.ecosta.2016.10.006>), and Bootstrap determination of the
co-integration rank (Cavaliere, G., Rahbek, A., & Taylor, A. M. R., 2012,
2014).

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
