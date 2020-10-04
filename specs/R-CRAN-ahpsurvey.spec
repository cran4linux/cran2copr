%global packname  ahpsurvey
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Analytic Hierarchy Process for Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-randomNames 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-randomNames 

%description
The Analytic Hierarchy Process is a versatile multi-criteria
decision-making tool introduced by Saaty (1987)
<doi:10.1016/0270-0255(87)90473-8> that allows decision-makers to weigh
attributes and evaluate alternatives presented to them.  This package
provides a consistent methodology for researchers to reformat data and run
analytic hierarchy process in R on data that are formatted using the
survey data entry mode. It is optimized for performing the analytic
hierarchy process with many decision-makers, and provides tools and
options for researchers to aggregate individual preferences and test
multiple options. It also allows researchers to quantify, visualize and
correct for inconsistency in the decision-maker's comparisons.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
