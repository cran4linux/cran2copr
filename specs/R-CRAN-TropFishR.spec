%global packname  TropFishR
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          3%{?dist}%{?buildtag}
Summary:          Tropical Fisheries Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-propagate 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-reshape2 
Requires:         R-MASS 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-propagate 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Hmisc 

%description
A compilation of fish stock assessment methods for the analysis of
length-frequency data in the context of data-poor fisheries. Includes
methods and examples included in the FAO Manual by P. Sparre and S.C.
Venema (1998), "Introduction to tropical fish stock assessment"
(<http://www.fao.org/documents/card/en/c/9bb12a06-2f05-5dcb-a6ca-2d6dd3080f65/>),
as well as other more recent methods.

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
