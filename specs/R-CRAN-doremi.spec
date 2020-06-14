%global packname  doremi
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Dynamics of Return to Equilibrium During Multiple Inputs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmerTest 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmerTest 

%description
Provides models to fit the dynamics of a regulated system experiencing
exogenous inputs. The underlying models use differential equations and
linear mixed-effects regressions to estimate the characteristic parameters
of the equation (the coefficients) and an estimated signal. The package
also provides print, summary, plot and predict functions, specific for the
models outputs.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
