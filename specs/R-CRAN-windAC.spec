%global packname  windAC
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          2%{?dist}
Summary:          Area Correction Methods

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-mvtnorm 

%description
Post-construction fatality monitoring studies at wind facilities are based
on data from searches for bird and bat carcasses in plots beneath
turbines. Bird and bat carcasses can fall outside of the search plot. Bird
and bat carcasses from wind turbines often fall outside of the searched
area. To compensate, area correction (AC) estimations are calculated to
estimate the percentage of fatalities that fall within the searched area
versus those that fall outside of it. This package provides two likelihood
based methods and one physics based method (Hull and Muir (2010)
<doi:10.1080/14486563.2010.9725253>, Huso and Dalthorp (2014)
<doi:10.1002/jwmg.663>) to estimate the carcass fall distribution. There
are also functions for calculating the proportion of area searched within
one unit annuli, log logistic distribution functions, and truncated
distribution functions.

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
%{rlibdir}/%{packname}/INDEX
