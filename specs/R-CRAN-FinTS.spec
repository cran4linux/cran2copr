%global packname  FinTS
%global packver   0.4-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          3%{?dist}
Summary:          Companion to Tsay (2005) Analysis of Financial Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-graphics 
Requires:         R-CRAN-zoo 
Requires:         R-graphics 

%description
R companion to Tsay (2005) Analysis of Financial Time Series, second
edition (Wiley). Includes data sets, functions and script files required
to work some of the examples.  Version 0.3-x includes R objects for all
data files used in the text and script files to recreate most of the
analyses in chapters 1-3 and 9 plus parts of chapters 4 and 11.

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
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
