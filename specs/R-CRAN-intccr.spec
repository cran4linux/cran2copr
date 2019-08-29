%global packname  intccr
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Semiparametric Competing Risks Regression under IntervalCensoring

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-alabama >= 2015.3.1
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-alabama >= 2015.3.1
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-utils 

%description
Semiparametric regression models on the cumulative incidence function with
interval-censored competing risks data as described in Bakoyannis, Yu, &
Yiannoutsos (2017) <doi:10.1002/sim.7350>. The main function fits the
proportional subdistribution hazards model (Fine-Gray model), the
proportional odds model, and other models that belong to the class of
semiparametric generalized odds rate transformation models.

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
%doc %{rlibdir}/%{packname}/citation
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/intccr.pdf
%{rlibdir}/%{packname}/INDEX
