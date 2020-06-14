%global packname  RcmdrPlugin.sampling
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Tools for sampling in Official Statistical Surveys

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcmdr 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-sampling 
Requires:         R-MASS 
Requires:         R-CRAN-Rcmdr 

%description
This package includes tools for calculating sample sizes and selecting
samples using various sampling designs. This package is an extension of
RcmdrPlugin.EHESsampling which was developed as part of the EHES pilot
project. The EHES Pilot project has received funding from the European
Commission and DG Sanco. The views expressed here are those of the authors
and they do not represent Commission's official position.

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
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
