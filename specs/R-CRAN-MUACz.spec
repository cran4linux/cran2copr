%global packname  MUACz
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Generate MUAC z-Scores for School Children Aged 5-19 Years Old

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-epiDisplay 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-epiDisplay 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 

%description
Generates mid upper arm circumference (MUAC) for age z-scores for children
and adolescents aged 5 to 19 years that can be used to assess nutritional
and health status and define risk of adverse health events. The standard
growth reference constructed by Mramba et. al (2017)
(<doi:10.1136/bmj.j3423>) smoothly join the WHO (2005) standards at age 5
years (<https://www.who.int/childgrowth/standards/Technical_report.pdf>)
and has been validated against mortality risk among children and
adolescents in Kenya, Uganda and Zimbabwe.

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
%{rlibdir}/%{packname}/INDEX
