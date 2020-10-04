%global packname  lineartestr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Linear Specification Testing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.2
Requires:         R-core > 3.2
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-forecast 
Requires:         R-Matrix 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-parallel 
Requires:         R-CRAN-forecast 

%description
Tests whether the linear hypothesis of a model is correct specified using
Dominguez-Lobato test. Also Ramsey's RESET (Regression Equation
Specification Error Test) test is implemented and Wald tests can be
carried out. Although RESET test is widely used to test the linear
hypothesis of a model, Dominguez and Lobato (2019) proposed a novel
approach that generalizes well known specification tests such as Ramsey's.
This test relies on wild-bootstrap; this package implements this approach
to be usable with any function that fits linear models and is compatible
with the update() function such as 'stats'::lm(), 'lfe'::felm() and
'forecast'::Arima(), for ARMA (autoregressive–moving-average) models. Also
the package can handle custom statistics such as Cramer von Mises and
Kolmogorov Smirnov, described by the authors, and custom distributions
such as Mammen (discrete and continuous) and Rademacher. Manuel A.
Dominguez & Ignacio N. Lobato (2019) <doi:10.1080/07474938.2019.1687116>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
