%global packname  CommonTrend
%global packver   0.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Extract and plot common trends from a cointegration system.Calculate P-value for Johansen Statistics.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-urca 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-urca 

%description
Directly extract and plot stochastic common trends from a cointegration
system using different approaches, currently including Kasa (1992) and
Gonzalo and Granger (1995). The approach proposed by Gonzalo and Granger,
also known as Permanent-Transitory Decomposition, is widely used in
macroeconomics and market microstructure literature. Kasa's approach, on
the other hand, has a nice property that it only uses the super consistent
estimator: the cointegration vector 'beta'. This package also provides
functions calculate P-value from Johansen Statistics according to the
approximation method proposed by Doornik (1998). Update: 0.7-1: Fix bugs
in calculation alpha. Add formulas and more explanations. 0.6-1: Rewrite
the description file. 0.5-1: Add functions to calculate P-value from
Johansen statistic, and vice versa.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
