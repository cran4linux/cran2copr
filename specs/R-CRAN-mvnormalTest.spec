%global packname  mvnormalTest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Powerful Tests for Multivariate Normality

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-copula 
Requires:         R-stats 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-copula 

%description
A simple informative powerful test (mvnTest()) for multivariate normality
proposed by Zhou and Shao (2014) <doi:10.1080/02664763.2013.839637>, which
combines kurtosis with Shapiro-Wilk test that is easy for biomedical
researchers to understand and easy to implement in all dimensions. This
package also contains some other multivariate normality tests including
Fattorini's FA test (faTest()), Mardia's skewness and kurtosis test
(mardia()), Henze-Zirkler's test (mhz()), Bowman and Shenton's test
(msk()), Royston’s H test (msw()), and Villasenor-Alva and
Gonzalez-Estrada's test (msw()). Empirical power calculation functions for
these tests are also provided. In addition, this package includes some
functions to generate several types of multivariate distributions
mentioned in Zhou and Shao (2014).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
