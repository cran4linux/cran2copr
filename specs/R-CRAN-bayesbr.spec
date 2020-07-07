%global packname  bayesbr
%global packver   0.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.1
Release:          2%{?dist}
Summary:          Beta Regression on a Bayesian Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-loo >= 2.2.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Formula >= 1.2.3
BuildRequires:    R-CRAN-fdrtool >= 1.2.15
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-loo >= 2.2.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-Formula >= 1.2.3
Requires:         R-CRAN-fdrtool >= 1.2.15
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RcppParallel 

%description
Applies the Beta regression model on the Bayesian statistical view, the
Beta regression is used when the response variable is a proportion
variable, that is, it only accepts values between 0 and 1. The package
'bayesbr' uses the package 'rstan' to build the Bayesian statistical
models. The main function of the package receives as a parameter a form
informing the independent variable and the co-variables of the model to be
made, as output it returns a list with the results of the model. For more
details see Ferrari and Cribari-Neto (2004)
<doi:10.1080/0266476042000214501> and Hoffman and Gelman (2014)
<arXiv:1111.4246>.

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
