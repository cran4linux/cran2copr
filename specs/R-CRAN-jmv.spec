%global packname  jmv
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          The 'jamovi' Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-psych >= 1.7.5
BuildRequires:    R-CRAN-emmeans >= 1.1.3
BuildRequires:    R-CRAN-jmvcore >= 1.0.8
BuildRequires:    R-CRAN-afex >= 0.20.2
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-PMCMR 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-vcdExtra 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-mvnormtest 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-nnet 
BuildRequires:    R-MASS 
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-psych >= 1.7.5
Requires:         R-CRAN-emmeans >= 1.1.3
Requires:         R-CRAN-jmvcore >= 1.0.8
Requires:         R-CRAN-afex >= 0.20.2
Requires:         R-CRAN-R6 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-PMCMR 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-vcdExtra 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-mvnormtest 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-ROCR 
Requires:         R-nnet 
Requires:         R-MASS 

%description
A suite of common statistical methods such as descriptives, t-tests,
ANOVAs, regression, correlation matrices, proportion tests, contingency
tables, and factor analysis. This package is also useable from the
'jamovi' statistical spreadsheet (see <https://www.jamovi.org> for more
information).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
