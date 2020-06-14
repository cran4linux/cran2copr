%global packname  otvPlots
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Over Time Variable Plots

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.33
BuildRequires:    R-grid >= 3.2.0
BuildRequires:    R-CRAN-Hmisc >= 3.17.4
BuildRequires:    R-CRAN-gridExtra >= 2.2.1
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-stringi >= 1.1.1
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-moments 
Requires:         R-CRAN-quantreg >= 5.33
Requires:         R-grid >= 3.2.0
Requires:         R-CRAN-Hmisc >= 3.17.4
Requires:         R-CRAN-gridExtra >= 2.2.1
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-stringi >= 1.1.1
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-moments 

%description
Enables automated visualization of variable distribution and changes over
time for predictive model building. It efficiently computes summary
statistics aggregated by time for large datasets, and create plots for
variable level monitoring.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
