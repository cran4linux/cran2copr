%global __brp_check_rpaths %{nil}
%global packname  BayesGWQS
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          2%{?dist}%{?buildtag}
Summary:          Bayesian Grouped Weighted Quantile Sum Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-CRAN-rjags 

%description
Fits Bayesian grouped weighted quantile sum (BGWQS) regressions for one or
more chemical groups with binary outcomes. Wheeler DC et al. (2019)
<doi:10.1016/j.sste.2019.100286>. Wheeler DC et al. (2020)
<doi:10.3390/ijerph17082864>.

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
