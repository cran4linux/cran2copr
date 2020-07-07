%global packname  opentripplanner
%global packver   0.2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3.0
Release:          3%{?dist}
Summary:          Setup and connect to 'OpenTripPlanner'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-vctrs >= 0.3.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-googlePolylines 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-vctrs >= 0.3.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-googlePolylines 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-pbapply 

%description
Setup and connect to 'OpenTripPlanner' (OTP)
<http://www.opentripplanner.org/>. OTP is an open source platform for
multi-modal and multi-agency journey planning written in 'Java'. The
package allows you to manage a local version or connect to remote OTP
server. This package has been peer-reviewed by rOpenSci (v. 0.2.0.0).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
