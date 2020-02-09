%global packname  SharpeR
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Statistical Significance of the Sharpe Ratio

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sadists >= 0.2.0
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-methods 
Requires:         R-CRAN-sadists >= 0.2.0
Requires:         R-CRAN-matrixcalc 
Requires:         R-methods 

%description
A collection of tools for analyzing significance of assets, funds, and
trading strategies, based on the Sharpe ratio and overfit of the same.
Provides density, distribution, quantile and random generation of the
Sharpe ratio distribution based on normal returns, as well as the optimal
Sharpe ratio over multiple assets. Computes confidence intervals on the
Sharpe and provides a test of equality of Sharpe ratios based on the Delta
method. The statistical foundations of the Sharpe can be found in the
author's Short Sharpe Course <doi:10.2139/ssrn.3036276>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
