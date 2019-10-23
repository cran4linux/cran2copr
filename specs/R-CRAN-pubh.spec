%global packname  pubh
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          A Toolbox for Public Health and Epidemiology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-tactile 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-desctable 
BuildRequires:    R-CRAN-effects 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-CRAN-epiR 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-nlme 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-papeR 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-survival 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-tactile 
Requires:         R-stats 
Requires:         R-CRAN-car 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-desctable 
Requires:         R-CRAN-effects 
Requires:         R-CRAN-Epi 
Requires:         R-CRAN-epiR 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-CRAN-multcomp 
Requires:         R-nlme 
Requires:         R-nnet 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-papeR 
Requires:         R-CRAN-sandwich 
Requires:         R-survival 

%description
A toolbox for making R functions and capabilities more accessible to
students and professionals from Epidemiology and Public Health related
disciplines. Includes a function to report coefficients and confidence
intervals from models using robust standard errors (when available),
functions that expand lattice plots and functions relevant for
introductory papers in Epidemiology or Public Health. Please note that use
of the provided data sets is for educational purposes only.

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
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
