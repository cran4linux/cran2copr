%global packname  arsenal
%global packver   3.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.0
Release:          2%{?dist}
Summary:          An Arsenal of 'R' Functions for Large-Scale StatisticalSummaries

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.2.0
BuildRequires:    R-utils >= 3.2.0
BuildRequires:    R-CRAN-knitr 
Requires:         R-stats >= 3.2.0
Requires:         R-utils >= 3.2.0
Requires:         R-CRAN-knitr 

%description
An Arsenal of 'R' functions for large-scale statistical summaries, which
are streamlined to work within the latest reporting tools in 'R' and
'RStudio' and which use formulas and versatile summary statistics for
summary tables and models. The primary functions include tableby(), a
Table-1-like summary of multiple variable types 'by' the levels of one or
more categorical variables; paired(), a Table-1-like summary of multiple
variable types paired across two time points; modelsum(), which performs
simple model fits on one or more endpoints for many variables (univariate
or adjusted for covariates); freqlist(), a powerful frequency table across
many categorical variables; comparedf(), a function for comparing
data.frames; and write2(), a function to output tables to a document.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
