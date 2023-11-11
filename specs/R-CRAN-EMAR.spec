%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMAR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Model Assessment

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A tool that allows users to generate various indices for evaluating
statistical models. The fitstat() function computes indices based on the
fitting data. The valstat() function computes indices based on the
validation data set. Both fitstat() and valstat() will return 16 indices
SSR: residual sum of squares, TRE: total relative error, Bias: mean bias,
MRB: mean relative bias, MAB: mean absolute bias, MAPE: mean absolute
percentage error, MSE: mean squared error, RMSE: root mean square error,
Percent.RMSE: percentage root mean squared error, R2: coefficient of
determination, R2adj: adjusted coefficient of determination, APC:
Amemiya's prediction criterion, logL: Log-likelihood, AIC: Akaike
information criterion, AICc: corrected Akaike information criterion, BIC:
Bayesian information criterion, HQC: Hannan-Quin information criterion.
The lower the better for the SSR, TRE, Bias, MRB, MAB, MAPE, MSE, RMSE,
Percent.RMSE, APC, AIC, AICc, BIC and HQC indices. The higher the better
for R2 and R2adj indices. Petre Stoica, P., Selén, Y. (2004)
<doi:10.1109/MSP.2004.1311138>n Zhou et al. (2023)
<doi:10.3389/fpls.2023.1186250>n Ogana, F.N., Ercanli, I. (2021)
<doi:10.1007/s11676-021-01373-1>n Musabbikhah et al. (2019)
<doi:10.1088/1742-6596/1175/1/012270>.

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
