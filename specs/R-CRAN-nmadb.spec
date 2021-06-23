%global __brp_check_rpaths %{nil}
%global packname  nmadb
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Network Meta-Analysis Database API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-jsonlite 

%description
Set of functions for accessing database of network meta-analyses described
in Petropoulou M, et al. Bibliographic study showed improving statistical
methodology of network meta-analyses published between 1999 and 2015
<doi:10.1016/j.jclinepi.2016.11.002>. The database is hosted in a REDcap
database at the Institute of Social and Preventive Medicine (ISPM) in the
University of Bern.

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
