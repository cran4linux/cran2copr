%global packname  imgrec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Image Recognition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.2
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-base64enc >= 0.1.0
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-knitr >= 1.2
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-base64enc >= 0.1.0

%description
Provides an interface for image recognition using the 'Google Vision API'
<https://cloud.google.com/vision/> .  Converts API data for features such
as object detection and optical character recognition to data frames. The
package also includes functions for analyzing image annotations.

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
%{rlibdir}/%{packname}/INDEX
