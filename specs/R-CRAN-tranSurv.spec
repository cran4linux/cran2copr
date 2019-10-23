%global packname  tranSurv
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Estimating a Survival Distribution in the Presence of DependentLeft Truncation and Right Censoring

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-methods 
Requires:         R-survival 
Requires:         R-CRAN-SQUAREM 
Requires:         R-methods 

%description
A structural transformation model for a latent, quasi-independent
truncation time as a function of the observed dependent truncation time
and the event time, and an unknown dependence parameter. The dependence
parameter is chosen to minimize the conditional Kendall's tau (Martin and
Betensky, 2005) <doi:10.1198/016214504000001538>. The marginal
distribution for the truncation time and the event time are completely
left unspecified.

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
%doc %{rlibdir}/%{packname}/bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
