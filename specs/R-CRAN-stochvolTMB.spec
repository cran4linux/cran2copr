%global __brp_check_rpaths %{nil}
%global packname  stochvolTMB
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood Estimation of Stochastic Volatility Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sn 
Requires:         R-stats 
Requires:         R-CRAN-data.table 

%description
Parameter estimation for stochastic volatility models using maximum
likelihood. The latent log-volatility is integrated out of the likelihood
using the Laplace approximation. The models are fitted via 'TMB' (Template
Model Builder) (Kristensen, Nielsen, Berg, Skaug, and Bell (2016)
<doi:10.18637/jss.v070.i05>).

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
