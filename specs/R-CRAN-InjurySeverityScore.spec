%global packname  InjurySeverityScore
%global packver   0.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.2
Release:          2%{?dist}
Summary:          Translate ICD-9 into Injury Severity Score

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 

%description
Calculate the injury severity score (ISS) based on the dictionary in
'ICDPIC' from <https://ideas.repec.org/c/boc/bocode/s457028.html>. The
original code was written in 'STATA 11'. The original 'STATA' code was
written by David Clark, Turner Osler and David Hahn. I implement the same
logic for easier access. Ref: David E. Clark & Turner M. Osler & David R.
Hahn, 2009. "ICDPIC: Stata module to provide methods for translating
International Classification of Diseases (Ninth Revision) diagnosis codes
into standard injury categories and/or scores," Statistical Software
Components S457028, Boston College Department of Economics, revised 29 Oct
2010.

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
