%global packname  modelStudio
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Interactive Studio for Explanatory Model Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-iBreakDown >= 1.0
BuildRequires:    R-CRAN-ingredients >= 1.0
BuildRequires:    R-CRAN-r2d3 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-iBreakDown >= 1.0
Requires:         R-CRAN-ingredients >= 1.0
Requires:         R-CRAN-r2d3 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-progress 

%description
Automate the explanatory analysis of machine learning predictive models.
This package generates advanced interactive and animated model
explanations in the form of a serverless HTML site with only one line of
code. The main function computes various (instance and dataset level)
model explanations and produces an interactive, customisable dashboard
made with 'D3.js'. It consists of multiple panels for plots with their
short descriptions. Easily save and share the dashboard with others. Tools
for model exploration unite with tools for EDA (Exploratory Data Analysis)
to give a broad overview of the model behavior.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/d3js
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
