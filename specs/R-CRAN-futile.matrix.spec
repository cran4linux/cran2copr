%global packname  futile.matrix
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}
Summary:          Random Matrix Generation and Manipulation

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-futile.logger >= 1.3.0
BuildRequires:    R-CRAN-lambda.r >= 1.1.6
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lambda.tools 
BuildRequires:    R-CRAN-RMTstat 
Requires:         R-CRAN-futile.logger >= 1.3.0
Requires:         R-CRAN-lambda.r >= 1.1.6
Requires:         R-utils 
Requires:         R-CRAN-lambda.tools 
Requires:         R-CRAN-RMTstat 

%description
A collection of functions for manipulating matrices and generating
ensembles of random matrices. Used primarily to identify the cutoff point
for the noise portion of the eigenvalue spectrum.

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
%{rlibdir}/%{packname}/sample-data
%{rlibdir}/%{packname}/INDEX
