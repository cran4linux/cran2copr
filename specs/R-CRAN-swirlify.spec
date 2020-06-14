%global packname  swirlify
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          2%{?dist}
Summary:          A Toolbox for Writing 'swirl' Courses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-swirl >= 2.4.2
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-swirl >= 2.4.2
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-readr 

%description
A set of tools for writing and sharing interactive courses to be used with
swirl.

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
%doc %{rlibdir}/%{packname}/swirlify-app
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
