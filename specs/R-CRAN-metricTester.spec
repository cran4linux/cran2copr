%global packname  metricTester
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}
Summary:          Test Metric and Null Model Statistical Performance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-spacodiR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-ape 
Requires:         R-methods 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-spacodiR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-MASS 
Requires:         R-CRAN-plotrix 

%description
Explore the behavior and statistical performance of 13 pre-defined
phylogenetic metrics and 11 null models, and of user-defined metrics and
null models, as detailed in Miller et al. (2017) <doi:10.1111/ecog.02070>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
