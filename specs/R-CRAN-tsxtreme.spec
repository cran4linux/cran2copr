%global packname  tsxtreme
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}
Summary:          Bayesian Modelling of Extremal Dependence in Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-graphics 

%description
Characterisation of the extremal dependence structure of time series,
avoiding pre-processing and filtering as done typically with
peaks-over-threshold methods. It uses the conditional approach of
Heffernan and Tawn (2004) <DOI:10.1111/j.1467-9868.2004.02050.x> which is
very flexible in terms of extremal and asymptotic dependence structures,
and Bayesian methods improve efficiency and allow for deriving measures of
uncertainty. For example, the extremal index, related to the size of
clusters in time, can be estimated and samples from its posterior
distribution obtained.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
