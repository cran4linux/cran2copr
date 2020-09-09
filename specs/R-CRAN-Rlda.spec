%global packname  Rlda
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian LDA for Mixed-Membership Clustering Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-Rcpp >= 0.9.4
BuildRequires:    R-CRAN-coda >= 0.19.1
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-Rcpp >= 0.9.4
Requires:         R-CRAN-coda >= 0.19.1
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-parallel 
Requires:         R-CRAN-gtools 

%description
Estimates the Bayesian LDA model for mixed-membership clustering based on
different types of data (i.e., Multinomial, Bernoulli, and Binomial
entries). Albuquerque, Valle and Li (2019)
<doi:10.1016/j.knosys.2018.10.024>.

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
