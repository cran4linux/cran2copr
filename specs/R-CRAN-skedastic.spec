%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  skedastic
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Handling Heteroskedasticity in the Linear Regression Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.47
BuildRequires:    R-CRAN-caret >= 6.0.90
BuildRequires:    R-CRAN-pracma >= 2.2.9
BuildRequires:    R-CRAN-Rfast >= 2.0.6
BuildRequires:    R-CRAN-mgcv >= 1.8.40
BuildRequires:    R-CRAN-quadprog >= 1.5.8
BuildRequires:    R-CRAN-CompQuadForm >= 1.4.3
BuildRequires:    R-CRAN-Matrix >= 1.4.1
BuildRequires:    R-CRAN-inflection >= 1.3.5
BuildRequires:    R-CRAN-ROI.plugin.qpoases >= 1.0.2
BuildRequires:    R-CRAN-bazar >= 1.0.11
BuildRequires:    R-CRAN-ROI >= 1.0.0
BuildRequires:    R-CRAN-osqp >= 0.6.0.5
BuildRequires:    R-CRAN-broom >= 0.5.6
BuildRequires:    R-CRAN-Rdpack >= 0.11
BuildRequires:    R-CRAN-slam >= 0.1.49
BuildRequires:    R-CRAN-quadprogXT >= 0.0.5
Requires:         R-CRAN-MASS >= 7.3.47
Requires:         R-CRAN-caret >= 6.0.90
Requires:         R-CRAN-pracma >= 2.2.9
Requires:         R-CRAN-Rfast >= 2.0.6
Requires:         R-CRAN-mgcv >= 1.8.40
Requires:         R-CRAN-quadprog >= 1.5.8
Requires:         R-CRAN-CompQuadForm >= 1.4.3
Requires:         R-CRAN-Matrix >= 1.4.1
Requires:         R-CRAN-inflection >= 1.3.5
Requires:         R-CRAN-ROI.plugin.qpoases >= 1.0.2
Requires:         R-CRAN-bazar >= 1.0.11
Requires:         R-CRAN-ROI >= 1.0.0
Requires:         R-CRAN-osqp >= 0.6.0.5
Requires:         R-CRAN-broom >= 0.5.6
Requires:         R-CRAN-Rdpack >= 0.11
Requires:         R-CRAN-slam >= 0.1.49
Requires:         R-CRAN-quadprogXT >= 0.0.5

%description
Implements numerous methods for testing for, modelling, and correcting for
heteroskedasticity in the classical linear regression model. The most
novel contribution of the package is found in the functions that implement
the as-yet-unpublished auxiliary linear variance models and auxiliary
nonlinear variance models that are designed to estimate error variances in
a heteroskedastic linear regression model. These models follow principles
of statistical learning described in Hastie (2009)
<doi:10.1007/978-0-387-21606-5>. The nonlinear version of the model is
estimated using quasi-likelihood methods as described in Seber and Wild
(2003, ISBN: 0-471-47135-6). Bootstrap methods for approximate confidence
intervals for error variances are implemented as described in Efron and
Tibshirani (1993, ISBN: 978-1-4899-4541-9), including also the expansion
technique described in Hesterberg (2014)
<doi:10.1080/00031305.2015.1089789>. The wild bootstrap employed here
follows the description in Davidson and Flachaire (2008)
<doi:10.1016/j.jeconom.2008.08.003>. Tuning of hyper-parameters makes use
of a golden section search function that is modelled after the MATLAB
function of Zarnowiec (2022)
<https://www.mathworks.com/matlabcentral/fileexchange/25919-golden-section-method-algorithm>.
A methodological description of the algorithm can be found in Fox (2021,
ISBN: 978-1-003-00957-3). There are 25 different functions that implement
hypothesis tests for heteroskedasticity. These include a test based on
Anscombe (1961) <https://projecteuclid.org/euclid.bsmsp/1200512155>,
Ramsey's (1969) BAMSET Test <doi:10.1111/j.2517-6161.1969.tb00796.x>, the
tests of Bickel (1978) <doi:10.1214/aos/1176344124>, Breusch and Pagan
(1979) <doi:10.2307/1911963> with and without the modification proposed by
Koenker (1981) <doi:10.1016/0304-4076(81)90062-2>, Carapeto and Holt
(2003) <doi:10.1080/0266476022000018475>, Cook and Weisberg (1983)
<doi:10.1093/biomet/70.1.1> (including their graphical methods), Diblasi
and Bowman (1997) <doi:10.1016/S0167-7152(96)00115-0>, Dufour, Khalaf,
Bernard, and Genest (2004) <doi:10.1016/j.jeconom.2003.10.024>, Evans and
King (1985) <doi:10.1016/0304-4076(85)90085-5> and Evans and King (1988)
<doi:10.1016/0304-4076(88)90006-1>, Glejser (1969)
<doi:10.1080/01621459.1969.10500976> as formulated by Mittelhammer, Judge
and Miller (2000, ISBN: 0-521-62394-4), Godfrey and Orme (1999)
<doi:10.1080/07474939908800438>, Goldfeld and Quandt (1965)
<doi:10.1080/01621459.1965.10480811>, Harrison and McCabe (1979)
<doi:10.1080/01621459.1979.10482544>, Harvey (1976) <doi:10.2307/1913974>,
Honda (1989) <doi:10.1111/j.2517-6161.1989.tb01749.x>, Horn (1981)
<doi:10.1080/03610928108828074>, Li and Yao (2019)
<doi:10.1016/j.ecosta.2018.01.001> with and without the modification of
Bai, Pan, and Yin (2016) <doi:10.1007/s11749-017-0575-x>, Rackauskas and
Zuokas (2007) <doi:10.1007/s10986-007-0018-6>, Simonoff and Tsai (1994)
<doi:10.2307/2986026> with and without the modification of Ferrari,
Cysneiros, and Cribari-Neto (2004) <doi:10.1016/S0378-3758(03)00210-6>,
Szroeter (1978) <doi:10.2307/1913831>, Verbyla (1993)
<doi:10.1111/j.2517-6161.1993.tb01918.x>, White (1980)
<doi:10.2307/1912934>, Wilcox and Keselman (2006)
<doi:10.1080/10629360500107923>, Yuce (2008)
<https://dergipark.org.tr/en/pub/iuekois/issue/8989/112070>, and Zhou,
Song, and Thompson (2015) <doi:10.1002/cjs.11252>. Besides these
heteroskedasticity tests, there are supporting functions that compute the
BLUS residuals of Theil (1965) <doi:10.1080/01621459.1965.10480851>, the
conditional two-sided p-values of Kulinskaya (2008) <arXiv:0810.2124v1>,
and probabilities for the nonparametric trend statistic of Lehmann (1975,
ISBN: 0-816-24996-1). For handling heteroskedasticity, in addition to the
new auxiliary variance model methods, there is a function to implement
various existing Heteroskedasticity-Consistent Covariance Matrix
Estimators from the literature, such as those of White (1980)
<doi:10.2307/1912934>, MacKinnon and White (1985)
<doi:10.1016/0304-4076(85)90158-7>, Cribari-Neto (2004)
<doi:10.1016/S0167-9473(02)00366-3>, Cribari-Neto et al. (2007)
<doi:10.1080/03610920601126589>, Cribari-Neto and da Silva (2011)
<doi:10.1007/s10182-010-0141-2>, Aftab and Chang (2016)
<doi:10.18187/pjsor.v12i2.983>, and Li et al. (2017)
<doi:10.1080/00949655.2016.1198906>.

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
