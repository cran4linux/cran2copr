%global packname  aurelius
%global packver   0.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.4
Release:          3%{?dist}%{?buildtag}
Summary:          Generates PFA Documents from R Code and Optionally Runs Them

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gbm >= 2.1.1
BuildRequires:    R-CRAN-glmnet >= 2.0.5
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-gbm >= 2.1.1
Requires:         R-CRAN-glmnet >= 2.0.5
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools for converting R objects and syntax into the Portable
Format for Analytics (PFA). Allows for testing validity and runtime
behavior of PFA documents through rPython and Titus, a more complete
implementation of PFA for Python. The Portable Format for Analytics is a
specification for event-based processors that perform predictive or
analytic calculations and is aimed at helping smooth the transition from
statistical model development to large-scale and/or online production. See
<http://dmg.org/pfa> for more information.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
