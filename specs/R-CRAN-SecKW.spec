%global packname  SecKW
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          The SecKW Distribution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-fdrtool 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-fdrtool 

%description
Density, distribution function, quantile function, random generation and
survival function for the Secant Kumaraswamy Weibull Distribution as
defined by SOUZA, L. New Trigonometric Class of Probabilistic
Distributions. 219 p. Thesis (Doctorate in Biometry and Applied
Statistics) - Department of Statistics and Information, Federal Rural
University of Pernambuco, Recife, Pernambuco, 2015 (available at
<http://www.openthesis.org/documents/New-trigonometric-classes-probabilistic-distributions-602633.html>)
and BRITO, C. C. R. Method Distributions generator and Probability
Distributions Classes. 241 p. Thesis (Doctorate in Biometry and Applied
Statistics) - Department of Statistics and Information, Federal Rural
University of Pernambuco, Recife, Pernambuco, 2014 (available upon
request).

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
