%global packname  lcpm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Ordinal Outcomes: Generalized Linear Models with the Log Link

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.2
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-Matrix >= 1.2.11
Requires:         R-stats >= 3.4.2
Requires:         R-CRAN-numDeriv >= 2016.8.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-Matrix >= 1.2.11

%description
An implementation of the Log Cumulative Probability Model (LCPM) and
Proportional Probability Model (PPM) for which the Maximum Likelihood
Estimates are determined using constrained optimization. This
implementation accounts for the implicit constraints on the parameter
space. Other features such as standard errors, z tests and p-values use
standard methods adapted from the results based on constrained
optimization.

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
