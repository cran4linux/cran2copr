%global __brp_check_rpaths %{nil}
%global packname  conformalInference.multi
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conformal Inference Tools for Regression with Multivariate Response

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-future.apply >= 1.8.1
BuildRequires:    R-CRAN-future >= 1.23.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-future.apply >= 1.8.1
Requires:         R-CRAN-future >= 1.23.0
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-stats 

%description
It computes full conformal, split conformal and multi split conformal
prediction regions when the response variable is multivariate (i.e.
dimension is greater than one). Moreover, the package also contain plot
functions to visualize the output of the full and split conformal
functions. To guarantee consistency, the package structure mimics the
univariate 'conformalInference' package of professor Ryan Tibshirani. The
main references for the code are: Lei et al. (2016) <arXiv:1604.04173>,
Diquigiovanni, Fontana, and Vantini (2021) <arXiv:2102.06746>,
Diquigiovanni, Fontana, and Vantini (2021) <arXiv:2106.01792>, Solari, and
Djordjilovic (2021) <arXiv:2103.00627>.

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
