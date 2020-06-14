%global packname  coxme
%global packver   2.2-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.16
Release:          2%{?dist}
Summary:          Mixed Effects Cox Models

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-survival >= 2.36.14
BuildRequires:    R-CRAN-bdsmatrix >= 1.3
BuildRequires:    R-Matrix >= 1.0
BuildRequires:    R-methods 
BuildRequires:    R-nlme 
Requires:         R-survival >= 2.36.14
Requires:         R-CRAN-bdsmatrix >= 1.3
Requires:         R-Matrix >= 1.0
Requires:         R-methods 
Requires:         R-nlme 

%description
Fit Cox proportional hazards models containing both fixed and random
effects.  The random effects can have a general form, of which familial
interactions (a "kinship" matrix) is a particular special case. Note that
the simplest case of a mixed effects Cox model, i.e. a single random
per-group intercept, is also called a "frailty" model.  The approach is
based on Ripatti and Palmgren, Biometrics 2002.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
