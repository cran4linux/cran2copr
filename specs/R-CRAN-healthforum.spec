%global packname  healthforum
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Scrape Patient Forum Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-stringr 

%description
Scrape data from Patient Forum <https://patient.info/forums> by entering
urls. It will return a data frame containing text, user names, like
counts, reply counts, etc.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
