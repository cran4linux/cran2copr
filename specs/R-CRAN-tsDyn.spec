%global __brp_check_rpaths %{nil}
%global packname  tsDyn
%global packver   10-1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          10.1.2
Release:          2%{?dist}%{?buildtag}
Summary:          Nonlinear Time Series Models with Regime Switching

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-mgcv 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-tseriesChaos 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
Requires:         R-CRAN-mnormt 
Requires:         R-mgcv 
Requires:         R-nnet 
Requires:         R-CRAN-tseriesChaos 
Requires:         R-CRAN-tseries 
Requires:         R-utils 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-forecast 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-methods 

%description
Implements nonlinear autoregressive (AR) time series models. For
univariate series, a non-parametric approach is available through additive
nonlinear AR. Parametric modeling and testing for regime switching
dynamics is available when the transition is either direct (TAR: threshold
AR) or smooth (STAR: smooth transition AR, LSTAR). For multivariate
series, one can estimate a range of TVAR or threshold cointegration TVECM
models with two or three regimes. Tests can be conducted for TVAR as well
as for TVECM (Hansen and Seo 2002 and Seo 2006).

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
