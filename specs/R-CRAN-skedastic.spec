%global packname  skedastic
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Heteroskedasticity Diagnostics for Linear Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-CRAN-car >= 3.0.5
BuildRequires:    R-CRAN-pracma >= 2.2.5
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
BuildRequires:    R-CRAN-lmtest >= 0.9.37
BuildRequires:    R-CRAN-Rmpfr >= 0.7.2
BuildRequires:    R-CRAN-broom >= 0.5.3
BuildRequires:    R-CRAN-gmp >= 0.5.13
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
BuildRequires:    R-CRAN-tseries >= 0.10.47
BuildRequires:    R-CRAN-het.test >= 0.1
Requires:         R-stats >= 3.5.0
Requires:         R-utils >= 3.5.0
Requires:         R-CRAN-car >= 3.0.5
Requires:         R-CRAN-pracma >= 2.2.5
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-matrixcalc >= 1.0.3
Requires:         R-CRAN-lmtest >= 0.9.37
Requires:         R-CRAN-Rmpfr >= 0.7.2
Requires:         R-CRAN-broom >= 0.5.3
Requires:         R-CRAN-gmp >= 0.5.13
Requires:         R-CRAN-Rdpack >= 0.11.0
Requires:         R-CRAN-tseries >= 0.10.47
Requires:         R-CRAN-het.test >= 0.1

%description
Implements numerous methods for detecting heteroskedasticity (sometimes
called heteroscedasticity) in the classical linear regression model. These
include the parametric and nonparametric tests of Goldfeld and Quandt
(1965) <doi:10.1080/01621459.1965.10480811>, the test of Glejser (1969)
<doi:10.1080/01621459.1969.10500976> as formulated by Mittelhammer, Judge
and Miller (2000, ISBN: 0-521-62394-4), the BAMSET Test of Ramsey (1969)
<doi:10.1111/j.2517-6161.1969.tb00796.x>, which uses the BLUS residuals
derived by Theil (1965) <doi:10.1080/01621459.1965.10480851>, the test of
Harvey (1976) <doi:10.2307/1913974>, the test of Breusch and Pagan (1979)
<doi:10.2307/1911963> with and without the modification proposed by
Koenker (1981) <doi:10.1016/0304-4076(81)90062-2>, the test of White
(1980) <doi:10.2307/1912934>, the test and graphical Cook and Weisberg
(1983) <doi:10.1093/biomet/70.1.1>, and the test of Li and Yao (2019)
<doi:10.1016/j.ecosta.2018.01.001>. Homoskedasticity refers to the
assumption of constant variance that is imposed on the model errors
(disturbances); heteroskedasticity is the violation of this assumption.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
