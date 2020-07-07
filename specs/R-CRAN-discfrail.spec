%global packname  discfrail
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Cox Models for Time-to-Event Data with Nonparametric DiscreteGroup-Specific Frailties

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-survival 
Requires:         R-Matrix 
Requires:         R-CRAN-numDeriv 

%description
Functions for fitting Cox proportional hazards models for grouped
time-to-event data, where the shared group-specific frailties have a
discrete nonparametric distribution. The methods proposed in the package
is described by Gasperoni, F., Ieva, F., Paganoni, A. M., Jackson, C. H.,
Sharples, L. (2018) <doi:10.1093/biostatistics/kxy071>. There are also
functions for simulating from these models, with a nonparametric or a
parametric baseline hazard function.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
