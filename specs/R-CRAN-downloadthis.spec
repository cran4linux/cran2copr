%global packname  downloadthis
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Implement Download Buttons in 'rmarkdown'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-zip 

%description
Implement download buttons in HTML output from 'rmarkdown' without the
need for 'runtime:shiny'.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/assets
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example
%{rlibdir}/%{packname}/INDEX
