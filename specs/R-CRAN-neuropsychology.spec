%global packname  neuropsychology
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Toolbox for Psychologists, Neuropsychologists andNeuroscientists

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-wordcloud2 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-htmlTable 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-png 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-wordcloud2 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-htmlTable 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-caret 

%description
Contains statistical functions (for patient assessment, data preprocessing
and reporting, ...) and datasets useful in psychology, neuropsychology and
neuroscience.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
