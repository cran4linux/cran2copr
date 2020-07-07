%global packname  HSPOR
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          3%{?dist}
Summary:          Hidden Smooth Polynomial Regression for Rupture Detection

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-npregfast 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-npregfast 
Requires:         R-graphics 

%description
Several functions that allow by different methods to infer a piecewise
polynomial regression model under regularity constraints, namely
continuity or differentiability of the link function. The implemented
functions are either specific to data with two regimes, or generic for any
number of regimes, which can be given by the user or learned by the
algorithm. A paper describing all these methods will be submitted soon.
The reference will be added to this file as soon as available.

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
