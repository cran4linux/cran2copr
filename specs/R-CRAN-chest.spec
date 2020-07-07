%global packname  chest
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Change-in-Estimate Approach to Assess Confounding Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.20
Requires:         R-core >= 2.20
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-survival 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-ggplot2 
Requires:         R-survival 
Requires:         R-grid 
Requires:         R-CRAN-speedglm 
Requires:         R-CRAN-forestplot 
Requires:         R-MASS 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 

%description
Applies the change-in-effect estimate method to assess confounding effects
in medical and epidemiological research (Greenland & Pearce (2016)
<doi:10.1146/annurev-publhealth-031914-122559> ). It starts with a crude
model including only the outcome and exposure variables. At each of the
subsequent steps, one variable which creates the largest change among the
remaining variables is selected. This process is repeated until all
variables have been entered into the model (Wang Z (2007)
<doi:10.1177/1536867X0700700203> ). Currently, the 'chest' package has
functions for linear regression, logistic regression, negative binomial
regression, Cox proportional hazards model and conditional logistic
regression.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
