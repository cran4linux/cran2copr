%global packname  intccr
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}
Summary:          Semiparametric Competing Risks Regression under Left Truncationand Interval Censoring with Missing Cause of Failure

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-alabama >= 2015.3.1
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-alabama >= 2015.3.1
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Semiparametric regression models on the cumulative incidence function for
interval-censored competing risks data as described in Bakoyannis, Yu, &
Yiannoutsos (2017) <doi:10.1002/sim.7350>, left-truncated and
interval-censored competing risks data, and interval-censored compering
risks data and missing cause of failure. We provide the proportional
subdistribution hazards model (Fine-Gray model), the proportional odds
model, and other models that belong to the class of semiparametric
generalized odds rate transformation models.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
