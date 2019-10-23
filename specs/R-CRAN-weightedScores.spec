%global packname  weightedScores
%global packver   0.9.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5.1
Release:          1%{?dist}
Summary:          Weighted Scores Method for Regression Models with Dependent Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rootSolve 

%description
Has functions to implement the weighted scores method and CL1 information
criteria as an intermediate step for variable/correlation selection for
longitudinal categorical and count data in Nikoloulopoulos, Joe and
Chaganty (2011, Biostatistics, 12: 653-665) and Nikoloulopoulos
(2015a,2015b).

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
%{rlibdir}/%{packname}/libs
