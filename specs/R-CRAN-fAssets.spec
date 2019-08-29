%global packname  fAssets
%global packver   3042.84
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3042.84
Release:          1%{?dist}
Summary:          Rmetrics - Analysing and Modelling Financial Assets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-fMultivar 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-ecodist 
BuildRequires:    R-CRAN-mvnormtest 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-fMultivar 
Requires:         R-CRAN-robustbase 
Requires:         R-MASS 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-ecodist 
Requires:         R-CRAN-mvnormtest 
Requires:         R-CRAN-energy 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides a collection of functions to manage, to investigate and to
analyze data sets of financial assets from different points of view.

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
%doc %{rlibdir}/%{packname}/obsolete
%{rlibdir}/%{packname}/INDEX
