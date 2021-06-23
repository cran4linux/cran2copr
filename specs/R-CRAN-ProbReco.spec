%global __brp_check_rpaths %{nil}
%global packname  ProbReco
%global packver   0.1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Score Optimal Probabilistic Forecast Reconciliation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-StanHeaders >= 2.19.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rdpack 

%description
Training of reconciliation weights for probabilistic forecasts to optimise
total energy (or variogram) score using Stochastic Gradient Descent with
automatically differentiated gradients. See Panagiotelis, Gamakumara,
Athanasopoulos and Hyndman, (2020)
<https://www.monash.edu/business/ebs/research/publications/ebs/wp26-2020.pdf>
for a description of the methods.

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
