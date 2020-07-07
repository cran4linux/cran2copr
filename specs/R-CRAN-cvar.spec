%global packname  cvar
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          Compute Expected Shortfall and Value at Risk for ContinuousDistributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.8
BuildRequires:    R-CRAN-gbutils 
BuildRequires:    R-CRAN-fGarch 
Requires:         R-CRAN-Rdpack >= 0.8
Requires:         R-CRAN-gbutils 
Requires:         R-CRAN-fGarch 

%description
Compute expected shortfall (ES) and Value at Risk (VaR) from a quantile
function, distribution function, random number generator or probability
density function.  ES is also known as Conditional Value at Risk (CVaR).
Virtually any continuous distribution can be specified. The functions are
vectorized over the arguments. The computations are done directly from the
definitions, see e.g. Acerbi and Tasche (2002)
<doi:10.1111/1468-0300.00091>. Some support for GARCH models is provided,
as well.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/auto
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
