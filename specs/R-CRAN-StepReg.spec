%global packname  StepReg
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Stepwise Regression Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.13

%description
Stepwise regression analysis for variable selection can be used to get the
best candidate final regression model with the forward selection, backward
elimination and bidirectional elimination approaches. Best subset
selection fit a separate least squares regression for each possible
combination of all predictors. Both the above two procedures in this
package can use weighted data to get best regression model in univariate
regression and multivariate regression analysis(Alsubaihi, A. A., (2002)
<doi:10.18637/jss.v007.i12>). And continuous variables nested within class
effect is also considered in both two procedures. Also stepwise logistic
regression in this package can performed with binary dependent
variable(Agresti, A. (1984) <doi:10.1002/9780470594001> and Agresti, A.
(2014) <doi:10.1007/978-3-642-04898-2_161>). A widely used selection
criteria are available which includes Akaike information
criterion(Darlington, R. B. (1968) <doi:10.1037/h0025471>, Judge, G. G.
(1985) <doi:10.2307/1391738>), corrected Akaike information
criterion(Hurvich, C. M., and Tsai, C. (1989)
<doi:10.1093/biomet/76.2.297>), Bayesian information criterion(Sawa, T.
(1978) <doi:10.2307/1913828>, Judge, G. G. (1985) <doi:10.2307/1391738>),
Mallows Cp statistic(Mallows, C. L. (1973)
<doi:10.1080/00401706.1995.10484370>, Hocking, R. R. (1976)
<doi:10.2307/2529336>), Hannan and Quinn information criterion(Hannan, E.
J. and Quinn, B. G. (1979) <doi:10.1111/j.2517-6161.1979.tb01072.x>,
Mcquarrie, A. D. R. and Tsai, C. L. (1998) <doi:10.1142/3573>), corrected
Hannan and Quinn information criterion(Mcquarrie, A. D. R. and Tsai, C. L.
(1998) <doi:10.1142/3573>), Schwarz criterion(Schwarz, G. (1978)
<doi:10.1214/aos/1176344136>, Judge, G. G. (1985) <doi:10.2307/1391738>),
adjusted R-square statistic(Darlington, R. B. (1968)
<doi:10.1037/h0025471>, Judge, G. G. (1985) <doi:10.2307/1391738>) and
significance levels(Mckeon, J. J. (1974) <doi:10.1093/biomet/61.2.381>,
Harold Hotelling. (1992) <doi:10.1007/978-1-4612-0919-5_4>, Pillai, K. C.
S. (2006) <doi:10.1002/0471667196.ess1965.pub2>), where multicollinearity
can be detected with checking tolerance value.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
