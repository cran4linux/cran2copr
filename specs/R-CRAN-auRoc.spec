%global packname  auRoc
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Various Methods to Estimate the AUC

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-MBESS >= 3.3.3
BuildRequires:    R-CRAN-rjags >= 3.11
BuildRequires:    R-CRAN-ProbYX >= 1.1
BuildRequires:    R-CRAN-coda >= 0.16.1
Requires:         R-CRAN-MBESS >= 3.3.3
Requires:         R-CRAN-rjags >= 3.11
Requires:         R-CRAN-ProbYX >= 1.1
Requires:         R-CRAN-coda >= 0.16.1

%description
Estimate the AUC using a variety of methods as follows: (1) frequentist
nonparametric methods based on the Mann-Whitney statistic or kernel
methods. (2) frequentist parametric methods using the likelihood ratio
test based on higher-order asymptotic results, the signed log-likelihood
ratio test, the Wald test, or the approximate ''t'' solution to the
Behrens-Fisher problem. (3) Bayesian parametric MCMC methods.

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
