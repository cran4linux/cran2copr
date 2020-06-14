%global packname  allestimates
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          2%{?dist}
Summary:          Effect Estimates from All Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-speedglm 
Requires:         R-survival 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 

%description
Estimates and plots effect estimates from models with all possible
combinations of a list of variables. It can be used for assessing
treatment effects in clinical trials or risk factors in bio-medical and
epidemiological research. Like Stata command 'confall' (Wang Z (2007)
<doi:10.1177/1536867X0700700203> ), 'allestimates' calculates and stores
all effect estimates, and plots them against p values or Akaike
information criterion (AIC) values. It currently has functions for linear
regression: all_lm(), logistic and Poisson regression: all_glm() and
all_speedglm(), and Cox proportional hazards regression: all_cox().

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
