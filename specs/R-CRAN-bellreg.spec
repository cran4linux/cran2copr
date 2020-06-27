%global packname  bellreg
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Count Regression Models Based on the Bell Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-magic 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-Rdpack 

%description
Bell regression models for count data with overdispersion. The implemented
models account for ordinary and zero-inflated regression models under both
frequentist and Bayesian approaches. Theoretical details regarding the
models implemented in the package can be found in Castellares et al.
(2018) <doi:10.1016/j.apm.2017.12.014> and Lemonte et al. (2020)
<doi:10.1080/02664763.2019.1636940>.

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
