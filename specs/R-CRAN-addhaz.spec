%global packname  addhaz
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          3%{?dist}
Summary:          Binomial and Multinomial Additive Hazard Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-boot >= 1.3.17
BuildRequires:    R-Matrix >= 1.2.3
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-boot >= 1.3.17
Requires:         R-Matrix >= 1.2.3
Requires:         R-stats 
Requires:         R-MASS 

%description
Functions to fit the binomial and multinomial additive hazard models and
to estimate the contribution of diseases/conditions to the disability
prevalence, as proposed by Nusselder and Looman (2004) and extended by
Yokota et al (2017).

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
