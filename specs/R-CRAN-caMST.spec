%global packname  caMST
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Mixed Computerized Adaptive Multistage Testing

License:          LGPL (>= 2.0, < 3) | Mozilla Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-catR 
BuildRequires:    R-CRAN-mstR 
Requires:         R-CRAN-catR 
Requires:         R-CRAN-mstR 

%description
Provides functions to more easily analyze computerized adaptive tests.
Currently, functions for computerized adaptive tests (CAT), computer
adaptive multistage tests (CMT), and mixed computer adaptive multistage
tests (McaMST) utilizing CAT item-level adaptation for the initial stage
and traditional MST module-level adaptation for the subsequent stages have
been created, and a variation of Hybrid computer adaptive MST is planned
as well. For an in-depth look at CAT and MST, see Weiss & Kingsbury (1984)
<doi:10.1111/j.1745-3984.1984.tb01040.x> and Luecht & Nungester (2000)
<doi:10.1007/0-306-47531-6_6> respectively.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
