%global packname  RESS
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Integrates R and Essentia

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Contains three functions that query AuriQ Systems' Essentia Database and
return the results in R. 'essQuery' takes a single Essentia command and
captures the output in R, where you can save the output to a dataframe or
stream it directly into additional analysis. 'read.essentia' takes an
Essentia script and captures the output csv data into R, where you can
save the output to a dataframe or stream it directly into additional
analysis. 'capture.essentia' takes a file containing any number of
Essentia commands and captures the output of the specified statements into
R dataframes. Essentia can be downloaded for free at
http://www.auriq.com/documentation/source/install/index.html.

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
%{rlibdir}/%{packname}/INDEX
