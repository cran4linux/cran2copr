%global packname  HSAR
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          2%{?dist}
Summary:          Hierarchical Spatial Autoregressive Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-spatialreg 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-spatialreg 
Requires:         R-CRAN-Rcpp 

%description
A Hierarchical Spatial Autoregressive Model (HSAR), based on a Bayesian
Markov Chain Monte Carlo (MCMC) algorithm (Dong and Harris (2014)
<doi:10.1111/gean.12049>). The creation of this package was supported by
the Economic and Social Research Council (ESRC) through the Applied
Quantitative Methods Network: Phase II, grant number ES/K006460/1.

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
