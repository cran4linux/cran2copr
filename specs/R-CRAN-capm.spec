%global packname  capm
%global packver   0.13.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.10
Release:          1%{?dist}
Summary:          Companion Animal Population Management

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-FME 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-FME 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-circlize 
Requires:         R-utils 
Requires:         R-CRAN-sf 

%description
Quantitative analysis to support companion animal population management.
Some functions assist survey sampling tasks (calculate sample size for
simple and complex designs, select sampling units and estimate population
parameters) while others assist the modelling of population dynamics. For
demographic characterizations and population management evaluations see:
"Baquero, et al." (2018), <doi:10.1016/j.prevetmed.2018.07.006>. For
modelling of population dynamics see: "Baquero et al." (2016),
<doi:10.1016/j.prevetmed.2015.11.009>. For sampling methods see: "Levy PS
& Lemeshow S" (2013), "ISBN-10: 0470040076"; "Lumley" (2010), "ISBN:
978-0-470-28430-8".

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
