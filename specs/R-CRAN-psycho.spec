%global packname  psycho
%global packver   0.4.91
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.91
Release:          1%{?dist}
Summary:          Efficient and Publishing-Oriented Workflow for PsychologicalScience

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-emmeans >= 1.2.2
BuildRequires:    R-CRAN-BayesFactor >= 0.9.1
BuildRequires:    R-CRAN-blavaan >= 0.3.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-nFactors 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-CRAN-rstantools 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-lavaan 
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-emmeans >= 1.2.2
Requires:         R-CRAN-BayesFactor >= 0.9.1
Requires:         R-CRAN-blavaan >= 0.3.4
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-psych 
Requires:         R-MASS 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-nFactors 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-rstanarm 
Requires:         R-CRAN-rstantools 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-lavaan 

%description
The main goal of the psycho package is to provide tools for psychologists,
neuropsychologists and neuroscientists, to facilitate and speed up the
time spent on data analysis. It aims at supporting best practices and
tools to format the output of statistical methods to directly paste them
into a manuscript, ensuring statistical reporting standardization and
conformity.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
