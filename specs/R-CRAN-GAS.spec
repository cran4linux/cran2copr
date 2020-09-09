%global packname  GAS
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Autoregressive Score Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-methods 
Requires:         R-CRAN-Rsolnp 
Requires:         R-MASS 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-cubature 

%description
Simulate, estimate and forecast using univariate and multivariate GAS
models as described in Ardia et al. (2019) <doi:10.18637/jss.v088.i06>.

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
