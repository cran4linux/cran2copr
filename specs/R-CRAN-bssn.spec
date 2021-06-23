%global __brp_check_rpaths %{nil}
%global packname  bssn
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Birnbaum-Saunders Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-ssmn 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ClusterR 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-ssmn 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ClusterR 

%description
It provides the density, distribution function, quantile function, random
number generator, reliability function, failure rate, likelihood function,
moments and EM algorithm for Maximum Likelihood estimators, also empirical
quantile and generated envelope for a given sample, all this for the three
parameter Birnbaum-Saunders model based on Skew-Normal Distribution. Also,
it provides the random number generator for the mixture of
Birnbaum-Saunders model based on Skew-Normal distribution. Additionally,
we incorporate the EM algorithm based on the assumption that the error
term follows a finite mixture of Sinh-normal distributions.

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
