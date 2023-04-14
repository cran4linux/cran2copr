%global __brp_check_rpaths %{nil}
%global packname  aRpsDCA
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Arps Decline Curve Analysis in R

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-methods 

%description
Functions for Arps decline-curve analysis on oil and gas data. Includes
exponential, hyperbolic, harmonic, and hyperbolic-to-exponential models as
well as the preceding with initial curtailment or a period of linear rate
buildup. Functions included for computing rate, cumulative production,
instantaneous decline, EUR, time to economic limit, and performing
least-squares best fits.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
