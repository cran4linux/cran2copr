%global packname  wru
%global packver   0.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          3%{?dist}
Summary:          Who are You? Bayesian Prediction of Racial Category UsingSurname and Geolocation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools >= 1.10.0
BuildRequires:    R-utils 
Requires:         R-CRAN-devtools >= 1.10.0
Requires:         R-utils 

%description
Predicts individual race/ethnicity using surname, geolocation, and other
attributes, such as gender and age. The method utilizes the Bayes' Rule to
compute the posterior probability of each racial category for any given
individual. The package implements methods described in Imai and Khanna
(2015) "Improving Ecological Inference by Predicting Individual Ethnicity
from Voter Registration Records" <DOI:10.1093/pan/mpw001>.

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
%{rlibdir}/%{packname}/INDEX
