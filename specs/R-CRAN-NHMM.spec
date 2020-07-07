%global packname  NHMM
%global packver   3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.11
Release:          2%{?dist}
Summary:          Bayesian Non-Homogeneous Markov and Mixture Models for MultipleTime Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-BayesLogit 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-MASS 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-BayesLogit 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-MCMCpack 
Requires:         R-MASS 

%description
Holsclaw, Greene, Robertson, and Smyth (2017) <doi:10.1214/16-AOAS1009>.
Bayesian HMM and NHMM modeling for multiple time series. The emission
distribution can be mixtures of Exponential, Gamma, Poisson, or Normal
distributions, and zero inflation is possible.

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
