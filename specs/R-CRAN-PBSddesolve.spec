%global __brp_check_rpaths %{nil}
%global packname  PBSddesolve
%global packver   1.12.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.6
Release:          3%{?dist}%{?buildtag}
Summary:          Solver for Delay Differential Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Functions for solving systems of delay differential equations by
interfacing with numerical routines written by Simon N. Wood, including
contributions from Benjamin J. Cairns. These numerical routines first
appeared in Simon Wood's 'solv95' program. This package includes a
vignette and a complete user's guide. 'PBSddesolve' originally appeared on
CRAN under the name 'ddesolve'. That version is no longer supported. The
current name emphasizes a close association with other 'PBS' packages,
particularly 'PBSmodelling'.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/demo_files
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
