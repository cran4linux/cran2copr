%global __brp_check_rpaths %{nil}
%global packname  anominate
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Alpha-NOMINATE Ideal Point Estimator

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-wnominate 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-wnominate 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-MCMCpack 

%description
Fits ideal point model described in Carroll, Lewis, Lo, Poole and
Rosenthal (2013), "The Structure of Utility in Models of Spatial Voting,"
American Journal of Political Science 57(4): 1008--1028,
<doi:10.1111/ajps.12029>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
