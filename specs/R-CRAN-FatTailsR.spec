%global packname  FatTailsR
%global packver   1.7-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.5
Release:          3%{?dist}
Summary:          Kiener Distributions and Fat Tails in Finance

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-timeSeries 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 

%description
Kiener distributions K1, K2, K3, K4 and K7 to characterize distributions
with left and right, symmetric or asymmetric fat tails in market finance,
neuroscience and other disciplines. Two algorithms to estimate with a high
accuracy distribution parameters, quantiles, value-at-risk and expected
shortfall. Include power hyperbolas and power hyperbolic functions.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
