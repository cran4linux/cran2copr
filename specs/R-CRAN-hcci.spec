%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hcci
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interval Estimation of Linear Models with Heteroskedasticity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Calculates the interval estimates for the parameters of linear models with
heteroscedastic regression using bootstrap - (Wild Bootstrap) and double
bootstrap-t (Wild Bootstrap). It is also possible to calculate confidence
intervals using the percentile bootstrap and percentile bootstrap double.
The package can calculate consistent estimates of the covariance matrix of
the parameters of linear regression models with heteroscedasticity of
unknown form. The package also provides a function to consistently
calculate the covariance matrix of the parameters of linear models with
heteroscedasticity of unknown form. The bootstrap methods exported by the
package are based on the master's thesis of the first author, available at
<https://raw.githubusercontent.com/prdm0/hcci/master/references/dissertacao_mestrado.pdf>.
The hcci package in previous versions was cited in the book VINOD,
Hrishikesh D. Hands-on Intermediate Econometrics Using R: Templates for
Learning Quantitative Methods and R Software. 2022, p. 441, ISBN
978-981-125-617-2 (hardcover). The simple bootstrap schemes are based on
the works of Cribari-Neto F and Lima M. G. (2009)
<doi:10.1080/00949650801935327>, while the double bootstrap schemes for
the parameters that index the linear models with heteroscedasticity of
unknown form are based on the works of Beran (1987) <doi:10.2307/2336685>.
The use of bootstrap for the calculation of interval estimates in
regression models with heteroscedasticity of unknown form from a weighting
of the residuals was proposed by Wu (1986) <doi:10.1214/aos/1176350142>.
This bootstrap scheme is known as weighted or wild bootstrap.

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
