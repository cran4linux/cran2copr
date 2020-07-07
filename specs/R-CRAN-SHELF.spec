%global packname  SHELF
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          3%{?dist}
Summary:          Tools to Support the Sheffield Elicitation Framework

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shinyMatrix 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-tidyr 
Requires:         R-MASS 
Requires:         R-CRAN-ggExtra 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rmarkdown 
Requires:         R-grDevices 
Requires:         R-CRAN-shinyMatrix 
Requires:         R-utils 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-Hmisc 

%description
Implements various methods for eliciting a probability distribution for a
single parameter from an expert or a group of experts. The expert provides
a small number of probability judgements, corresponding to points on his
or her cumulative distribution function. A range of parametric
distributions can then be fitted and displayed, with feedback provided in
the form of fitted probabilities and percentiles. For multiple experts, a
weighted linear pool can be calculated. Also includes functions for
eliciting beliefs about population distributions, eliciting multivariate
distributions using a Gaussian copula, eliciting a Dirichlet distribution,
and eliciting distributions for variance parameters in a random effects
meta-analysis model. R Shiny apps for most of the methods are included.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/elicitationReportFile
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/shinyAppFiles
%{rlibdir}/%{packname}/INDEX
