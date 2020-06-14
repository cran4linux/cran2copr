%global packname  spread
%global packver   2019.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.8.5
Release:          2%{?dist}
Summary:          Infectious Disease Spread Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.9.4
BuildRequires:    R-CRAN-RcppProgress >= 0.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fhidata 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-Rcpp >= 0.9.4
Requires:         R-CRAN-RcppProgress >= 0.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fhidata 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-zoo 

%description
A stochastic SEIIaR (susceptible, exposed, infectious, infectious
asymptomatic, recovered) metapopulation model that including commuting.
Each location has a local infection system, while the locations are
connected by people who commute each day. The model differentiates between
day and night. During the day you can infect/be infected in the location
where you work, while during the night you can infect/be infected in the
location where you live. It is the same commuters who travel back and
forth each day. At the start of a day, all commuters are sent to their
work location, where they mix for 12 hours. The commuters are then sent to
their respective home locations, where they mix for 12 hours. The model is
loosely based upon a published model by Engebretsen (2019)
<doi:10.1371/journal.pcbi.1006879>.

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
%doc %{rlibdir}/%{packname}/cpp
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
