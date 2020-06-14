%global packname  swirl
%global packver   2.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.5
Release:          2%{?dist}
Summary:          Learn R, in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-testthat >= 1.0.2
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-tools 
BuildRequires:    R-methods 
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-testthat >= 1.0.2
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-digest 
Requires:         R-tools 
Requires:         R-methods 

%description
Use the R console as an interactive learning environment. Users receive
immediate feedback as they are guided through self-paced lessons in data
science and R programming.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Courses
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
