%global packname  BBEST
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Bayesian Estimation of Incoherent Neutron Scattering Backgrounds

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-wmtsa 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-methods 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-wmtsa 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-shiny 
Requires:         R-methods 

%description
We implemented a Bayesian-statistics approach for subtraction of
incoherent scattering from neutron total-scattering data. In this
approach, the estimated background signal associated with incoherent
scattering maximizes the posterior probability, which combines the
likelihood of this signal in reciprocal and real spaces with the prior
that favors smooth lines.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/gui
%doc %{rlibdir}/%{packname}/progress
%{rlibdir}/%{packname}/INDEX
