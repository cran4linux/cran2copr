%global packname  gnFit
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Goodness of Fit Test for Continuous Distribution Functions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-rmutil 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-rmutil 

%description
Computes the test statistic and p-value of the Cramer-von Mises and
Anderson-Darling test for some continuous distribution functions proposed
by Chen and Balakrishnan (1995)
<http://asq.org/qic/display-item/index.html?item=11407>. In addition to
our classic distribution functions here, we calculate the Goodness of Fit
(GoF) test to dataset which follows the extreme value distribution
function, without remembering the formula of distribution/density
functions. Calculates the Value at Risk (VaR) and Average VaR are another
important risk factors which are estimated by using well-known
distribution functions. Pflug and Romisch (2007, ISBN: 9812707409) is a
good reference to study the properties of risk measures.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
