%global packname  tableone
%global packver   0.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.1
Release:          1%{?dist}
Summary:          Create 'Table 1' to Describe Baseline Characteristics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-labelled 
Requires:         R-CRAN-survey 
Requires:         R-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-gmodels 
Requires:         R-nlme 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-labelled 

%description
Creates 'Table 1', i.e., description of baseline patient characteristics,
which is essential in every medical research. Supports both continuous and
categorical variables, as well as p-values and standardized mean
differences. Weighted data are supported via the 'survey' package. See
'github' for a screen cast. 'tableone' was inspired by descriptive
statistics functions in 'Deducer' , a Java-based GUI package by Ian
Fellows. This package does not require GUI or Java, and intended for
command-line users.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
