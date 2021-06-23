%global __brp_check_rpaths %{nil}
%global packname  pssm
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Piecewise Exponential Model for Time to Progression and Timefrom Progression to Death

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MHadaptive 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MHadaptive 

%description
Estimates parameters of a piecewise exponential model for time to
progression and time from progression to death with interval censoring of
the time to progression and covariates for each distribution using
proportional hazards.

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
