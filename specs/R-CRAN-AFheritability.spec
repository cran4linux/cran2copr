%global packname  AFheritability
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          The Attributable Fraction (AF) Described as a Function ofDisease Heritability, Prevalence and Intervention SpecificFactors

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 

%description
The AFfunction() is a function which returns an estimate of the
Attributable Fraction (AF) and a plot of the AF as a function of
heritability, disease prevalence, size of target group and intervention
effect. Since the AF is a function of several factors, a shiny app is used
to better illustrate how the relationship between the AF and heritability
depends on several other factors. The app is ran by the function
runShinyApp(). For more information see Dahlqwist E et al. (2019)
<doi:10.1007/s00439-019-02006-8>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
