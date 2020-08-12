%global packname  skedastic
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Heteroskedasticity Diagnostics for Linear Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-CRAN-quantreg >= 5.55
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-pracma >= 2.2.9
BuildRequires:    R-CRAN-plm >= 2.2.0
BuildRequires:    R-CRAN-cubature >= 2.0.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-CompQuadForm >= 1.4.3
BuildRequires:    R-CRAN-shiny >= 1.4.0.2
BuildRequires:    R-boot >= 1.3.24
BuildRequires:    R-CRAN-berryFunctions >= 1.17
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-arrangements >= 1.1.8
BuildRequires:    R-CRAN-mvtnorm >= 1.1.0
BuildRequires:    R-CRAN-qpdf >= 1.1
BuildRequires:    R-CRAN-bazar >= 1.0.11
BuildRequires:    R-CRAN-expm >= 0.999.4
BuildRequires:    R-CRAN-Rmpfr >= 0.8.0
BuildRequires:    R-CRAN-broom >= 0.5.6
BuildRequires:    R-CRAN-gmp >= 0.5.13
BuildRequires:    R-CRAN-Rdpack >= 0.11.1
Requires:         R-MASS >= 7.3.47
Requires:         R-CRAN-quantreg >= 5.55
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-pracma >= 2.2.9
Requires:         R-CRAN-plm >= 2.2.0
Requires:         R-CRAN-cubature >= 2.0.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-CompQuadForm >= 1.4.3
Requires:         R-CRAN-shiny >= 1.4.0.2
Requires:         R-boot >= 1.3.24
Requires:         R-CRAN-berryFunctions >= 1.17
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-arrangements >= 1.1.8
Requires:         R-CRAN-mvtnorm >= 1.1.0
Requires:         R-CRAN-qpdf >= 1.1
Requires:         R-CRAN-bazar >= 1.0.11
Requires:         R-CRAN-expm >= 0.999.4
Requires:         R-CRAN-Rmpfr >= 0.8.0
Requires:         R-CRAN-broom >= 0.5.6
Requires:         R-CRAN-gmp >= 0.5.13
Requires:         R-CRAN-Rdpack >= 0.11.1

%description
Implements numerous methods for detecting heteroskedasticity (sometimes
called heteroscedasticity) in the classical linear regression model. These
include a test based on Anscombe (1961) <https://projecteuclid.org/
euclid.bsmsp/1200512155>, Ramsey's (1969) BAMSET Test
<doi:10.1111/j.2517-6161.1969.tb00796.x>, the tests of Bickel (1978)
<doi:10.1214/aos/1176344124>, Breusch and Pagan (1979)
<doi:10.2307/1911963> with and without the modification proposed by
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
<doi:10.1080/01621459.1965.10480811>, Harvey (1976) <doi:10.2307/1913974>,
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
<doi:10.1080/10629360500107923>, and Zhou, Song, and Thompson (2015)
<doi:10.1002/cjs.11252>. Besides these heteroskedasticity tests, there are
supporting functions that compute the BLUS residuals of Theil (1965)
<doi:10.1080/01621459.1965.10480851>, the conditional two-sided p-values
of Kulinskaya (2008) <arXiv:0810.2124v1>, and probabilities for the
nonparametric trend statistic of Lehmann (1975, ISBN: 0-816-24996-1).
Homoskedasticity refers to the assumption of constant variance that is
imposed on the model errors (disturbances); heteroskedasticity is the
violation of this assumption.

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
