%global packname  MGBT
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          Multiple Grubbs-Beck Low-Outlier Test

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Compute the multiple Grubbs-Beck low-outlier test on positively
distributed data and utilities for noninterpretive U.S. Geological Survey
annual peak-streamflow data processing discussed in Cohn et al. (2013)
<doi:10.1002/wrcr.20392> and England et al. (2017) <doi:10.3133/tm4B5>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/helpers
%doc %{rlibdir}/%{packname}/INSTALL_HELP.md
%doc %{rlibdir}/%{packname}/legend
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/sources
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
