%global packname  radiant.design
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}
Summary:          Design Menu for Radiant: Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.2.0
BuildRequires:    R-CRAN-AlgDesign >= 1.1.7.3
BuildRequires:    R-CRAN-pwr >= 1.1.2
BuildRequires:    R-CRAN-import >= 1.1.0
BuildRequires:    R-CRAN-radiant.data >= 0.9.7
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-polycor 
Requires:         R-CRAN-shiny >= 1.2.0
Requires:         R-CRAN-AlgDesign >= 1.1.7.3
Requires:         R-CRAN-pwr >= 1.1.2
Requires:         R-CRAN-import >= 1.1.0
Requires:         R-CRAN-radiant.data >= 0.9.7
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-polycor 

%description
The Radiant Design menu includes interfaces for design of experiments,
sampling, and sample size calculation. The application extends the
functionality in radiant.data.

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
%doc %{rlibdir}/%{packname}/app
%{rlibdir}/%{packname}/INDEX
