%global packname  REREFACT
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Reordering and/or Reflecting Factors for Simulation Studies withExploratory Factor Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-methods 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-combinat 
Requires:         R-Matrix 
Requires:         R-CRAN-gdata 
Requires:         R-methods 

%description
Executes a post-rotation algorithm that REorders and/or REflects FACTors
(REREFACT) for each replication of a simulation study with exploratory
factor analysis.

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
%{rlibdir}/%{packname}/INDEX
