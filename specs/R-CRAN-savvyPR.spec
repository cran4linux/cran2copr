%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  savvyPR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Savvy Parity Regression Model Estimation with 'savvyPR'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Implements the Savvy Parity Regression 'savvyPR' methodology for
multivariate linear regression analysis. The package solves an
optimization problem that balances the contribution of each predictor
variable to ensure estimation stability in the presence of
multicollinearity. It supports two distinct parameterization methods, a
Budget-based approach that allocates a fixed loss contribution to each
predictor, and a Target-based approach (t-tuning) that utilizes a relative
elasticity weight for the response variable. The package provides
comprehensive tools for model estimation, risk distribution analysis, and
parameter tuning via cross-validation (PR1, PR2, and PR3 model types) to
optimize predictive accuracy. Methods are based on Asimit, Chen, Ichim and
Millossovich (2026) <https://openaccess.city.ac.uk/id/eprint/35005/>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
