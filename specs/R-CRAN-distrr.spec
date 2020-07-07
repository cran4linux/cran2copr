%global packname  distrr
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          3%{?dist}
Summary:          Estimate and Manage Empirical Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-tidyr >= 0.7.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-tidyr >= 0.7.0
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-stats 

%description
Tools to estimate and manage empirical distributions, which should work
with survey data. One of the main features is the possibility to create
data cubes of estimated statistics, that include all the combinations of
the variables of interest (see for example functions dcc5() and dcc6()).

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
%{rlibdir}/%{packname}/INDEX
