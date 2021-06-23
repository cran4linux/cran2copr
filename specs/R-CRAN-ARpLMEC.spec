%global __brp_check_rpaths %{nil}
%global packname  ARpLMEC
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Fitting Autoregressive Censored Mixed-Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lmec 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-Matrix 
Requires:         R-stats4 
Requires:         R-CRAN-gmm 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-lmec 
Requires:         R-CRAN-mnormt 

%description
It fits left, right or intervalar censored mixed-effects linear model with
autoregressive errors of order p using the EM algorithm. It provides
estimates, standard errors of the parameters and prediction of future
observations. Florin Vaida and Lin Liu (2009)
<doi:10.1198/jcgs.2009.07130>.

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
