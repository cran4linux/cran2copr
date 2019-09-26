%global packname  gestate
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Generalised Survival Trial Assessment Tool Environment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-survRM2 
BuildRequires:    R-survival 
BuildRequires:    R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-survRM2 
Requires:         R-survival 
Requires:         R-methods 

%description
Provides tools to assist planning and monitoring of time-to-event trials
under complicated censoring assumptions and/or non-proportional hazards.
There are three main components: The first is analytic calculation of
predicted time-to-event trial properties, providing estimates of expected
hazard ratio, event numbers and power under different analysis methods.
The second is simulation, allowing calculation of these same properties.
Finally, it also provides parametric event prediction using blinded trial
data, including creation of confidence intervals. Methods are based upon
numerical integration and a flexible object-orientated structure for
defining event, censoring and recruitment curves.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Shiny
%{rlibdir}/%{packname}/INDEX
