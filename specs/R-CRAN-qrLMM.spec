%global packname  qrLMM
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Quantile Regression for Linear Mixed-Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-lqr 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-ald 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-lqr 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-psych 
Requires:         R-tcltk 
Requires:         R-CRAN-ald 

%description
Quantile regression (QR) for Linear Mixed-Effects Models via the
asymmetric Laplace distribution (ALD). It uses the Stochastic
Approximation of the EM (SAEM) algorithm for deriving exact maximum
likelihood estimates and full inference results for the fixed-effects and
variance components. It also provides graphical summaries for assessing
the algorithm convergence and fitting results.

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
