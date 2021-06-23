%global __brp_check_rpaths %{nil}
%global packname  facerec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          4%{?dist}%{?buildtag}
Summary:          An Interface for Face Recognition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-httr >= 1.3.0
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-knitr >= 1.2
BuildRequires:    R-CRAN-snakecase >= 0.9.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-httr >= 1.3.0
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-knitr >= 1.2
Requires:         R-CRAN-snakecase >= 0.9.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rlang 

%description
Provides an interface to the 'Kairos' Face Recognition API
<https://kairos.com/face-recognition-api>. The API detects faces in images
and returns estimates for demographics like gender, ethnicity and age.

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
