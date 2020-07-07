%global packname  aMNLFA
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          Automated Fitting of Moderated Nonlinear Factor Analysis Throughthe 'Mplus' Program

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-devtools 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-devtools 

%description
Automated generation, running, and interpretation of moderated nonlinear
factor analysis models for obtaining scores from observed variables. This
package creates 'Mplus' input files which may be run iteratively to test
two different types of covariate effects on items: (1) latent variable
impact (both mean and variance); and (2) differential item functioning.
After sequentially testing for all effects, it also creates a final model
by including all significant effects after adjusting for multiple
comparisons. Finally, the package creates a scoring model which uses the
final values of parameter estimates to generate latent variable scores.

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
%doc %{rlibdir}/%{packname}/examplefiles
%{rlibdir}/%{packname}/INDEX
