%global packname  chest
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Change-in-Estimate Approach to Assess Confounding Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-survival 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-tidyverse 
Requires:         R-survival 
Requires:         R-grid 
Requires:         R-CRAN-speedglm 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tibble 
Requires:         R-MASS 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyselect 

%description
The 'chest' package applies the change-in-effect estimate method for
assessing confounding effects in medical and epidemiological research. It
starts with a crude model including only the outcome and exposure
variables. At each of the subsequent steps, one variable which creates the
largest change among the remaining variables is selected. This process is
repeated until all variables have been entered into the model (Wang Z
(2007) <doi:10.1177/1536867X0700700203>). Currently, the 'chest' package
has functions for linear regression, logistic regression, Cox proportional
hazards model and conditional logistic regression.

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
