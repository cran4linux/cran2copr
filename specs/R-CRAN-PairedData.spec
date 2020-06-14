%global packname  PairedData
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Paired Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gld 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-gld 
Requires:         R-CRAN-mvtnorm 
Requires:         R-lattice 
Requires:         R-CRAN-ggplot2 

%description
Many datasets and a set of graphics (based on ggplot2), statistics, effect
sizes and hypothesis tests are provided for analysing paired data with S4
class.

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
