%global packname  eha
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          1%{?dist}
Summary:          Event History Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-survival >= 2.42.5
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-survival >= 2.42.5
Requires:         R-stats 
Requires:         R-graphics 

%description
Sampling of risk sets in Cox regression, selections in the Lexis diagram,
bootstrapping. Parametric proportional hazards fitting with left
truncation and right censoring for common families of distributions,
piecewise constant hazards, and discrete models. Parametric accelerated
failure time models for left truncated and right censored data.

%prep
%setup -q -c -n %{packname}


%build

%install
test $(gcc -dumpversion) -ge 10 && export PKG_FFLAGS=-fallow-argument-mismatch
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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
