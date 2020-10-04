%global packname  monotonicity
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Test for Monotonicity in Expected Asset Returns, Sorted byPortfolios

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-lmtest 
Requires:         R-MASS 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 

%description
Test for monotonicity in financial variables sorted by portfolios. It is
conventional practice in empirical research to form portfolios of assets
ranked by a certain sort variable. A t-test is then used to consider the
mean return spread between the portfolios with the highest and lowest
values of the sort variable. Yet comparing only the average returns on the
top and bottom portfolios does not provide a sufficient way to test for a
monotonic relation between expected returns and the sort variable. This
package provides nonparametric tests for the full set of monotonic
patterns by Patton, A. and Timmermann, A. (2010)
<doi:10.1016/j.jfineco.2010.06.006> and compares the proposed results with
extant alternatives such as t-tests, Bonferroni bounds, and multivariate
inequality tests through empirical applications and simulations.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
