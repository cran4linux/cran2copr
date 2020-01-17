%global packname  Epi
%global packver   2.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.40
Release:          1%{?dist}
Summary:          A Package for Statistical Analysis in Epidemiology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-etm 
BuildRequires:    R-splines 
BuildRequires:    R-MASS 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-mgcv 
Requires:         R-utils 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-etm 
Requires:         R-splines 
Requires:         R-MASS 
Requires:         R-survival 
Requires:         R-CRAN-plyr 
Requires:         R-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-zoo 
Requires:         R-mgcv 

%description
Functions for demographic and epidemiological analysis in the Lexis
diagram, i.e. register and cohort follow-up data, in particular
representation, manipulation and simulation of multistate data - the Lexis
suite of functions, which includes interfaces to 'mstate', 'etm' and
'cmprsk' packages. Also contains functions for Age-Period-Cohort and
Lee-Carter modeling and a function for interval censored data and some
useful functions for tabulation and plotting, as well as a number of
epidemiological data sets.

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
%{rlibdir}/%{packname}/libs
