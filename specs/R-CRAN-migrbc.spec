%global packname  migrbc
%global packver   2.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.9
Release:          3%{?dist}
Summary:          Production Rules Based Classification of Migration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-lubridate >= 1.7
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-Rcpp >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-futile.logger 
Requires:         R-CRAN-lubridate >= 1.7
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-futile.logger 

%description
Provides mechanisms for classifying border crossings using a rules-based
methodology. The goal of performing this type of classification is to
identify any potential long-term migrants.  A long-term migration is
defined as a border crossing involving a change in residence status. A
border crossing counts as a long-term migration to/from a country if it
entails a change from non-residence to residence / residence to
non-residence.  The rules-based classification that used to determine a
long-term migration is defined by a threshold duration and a test
duration, alternatively named window size. Under a 12/16 rule, for
instance, the threshold duration is 12 months and the test duration
(window size) is 16 months. With a 9/12 rule, the threshold duration is 9
months and the test duration (window size) is 12 months. For more
information about the methodology applied, please visit Stats NZ (2020)
<https://www.stats.govt.nz/methods/defining-migrants-using-travel-histories-and-the-1216-month-rule>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
