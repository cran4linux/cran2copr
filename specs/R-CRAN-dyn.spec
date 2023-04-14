%global __brp_check_rpaths %{nil}
%global packname  dyn
%global packver   0.2-9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9.6
Release:          3%{?dist}%{?buildtag}
Summary:          Time Series Regression

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.0.0
Requires:         R-CRAN-zoo >= 1.0.0

%description
Time series regression.  The dyn class interfaces ts, irts(), zoo() and
zooreg() time series classes to lm(), glm(), loess(), quantreg::rq(),
MASS::rlm(), MCMCpack::MCMCregress(), quantreg::rq(),
randomForest::randomForest() and other regression functions allowing those
functions to be used with time series including specifications that may
contain lags, diffs and missing values.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
