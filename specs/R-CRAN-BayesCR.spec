%global __brp_check_rpaths %{nil}
%global packname  BayesCR
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Censored Regression Models Under ScaleMixture of Skew Normal Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mnormt 

%description
Propose a parametric fit for censored linear regression models based on
SMSN distributions, from a Bayesian perspective. Also, generates SMSN
random variables.

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
