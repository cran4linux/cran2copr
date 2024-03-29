%global __brp_check_rpaths %{nil}
%global packname  rMR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Importing Data from Loligo Systems Software, CalculatingMetabolic Rates and Critical Tensions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-biglm 
Requires:         R-CRAN-biglm 

%description
Analysis of oxygen consumption data generated by Loligo (R) Systems
respirometry equipment. The package includes a function for loading data
output by Loligo's 'AutoResp' software (get.witrox.data()), functions for
calculating metabolic rates over user-specified time intervals, extracting
critical points from data using broken stick regressions based on Yeager
and Ultsch (<DOI:10.1086/physzool.62.4.30157935>), and easy functions for
converting between different units of barometric pressure.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
