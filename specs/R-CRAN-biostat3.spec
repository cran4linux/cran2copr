%global packname  biostat3
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}
Summary:          Utility Functions, Datasets and Extended Examples for SurvivalAnalysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-muhaz 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-survival 
Requires:         R-MASS 
Requires:         R-CRAN-muhaz 
Requires:         R-CRAN-car 
Requires:         R-graphics 
Requires:         R-stats 

%description
Utility functions, datasets and extended examples for survival analysis.
This extends a range of other packages, some simple wrappers for
time-to-event analyses, datasets, and extensive examples in HTML with R
scripts. The package also supports the course Biostatistics III entitled
"Survival analysis for epidemiologists in R".

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
