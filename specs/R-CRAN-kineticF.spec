%global packname  kineticF
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Framework for the Analysis of Kinetic Visual Field Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.1.0
Requires:         R-core > 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-lqmm 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-MASS 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-lqmm 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-plotrix 
Requires:         R-MASS 

%description
Data cleaning, processing, visualisation and analysis for manual
(Goldmann) and automated (Octopus 900) kinetic visual field data.

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
