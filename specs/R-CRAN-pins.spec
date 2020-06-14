%global packname  pins
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          2%{?dist}
Summary:          Pin, Discover and Share Resources

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-backports 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-zip 

%description
Pin remote resources into a local cache to work offline, improve speed and
avoid recomputing; discover and share resources in local folders,
'GitHub', 'Kaggle' or 'RStudio Connect'. Resources can be anything from
'CSV', 'JSON', or image files to arbitrary R objects.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/icons
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/views
%{rlibdir}/%{packname}/INDEX
