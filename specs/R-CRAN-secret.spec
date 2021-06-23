%global __brp_check_rpaths %{nil}
%global packname  secret
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Share Sensitive Information in R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 

%description
Allow sharing sensitive information, for example passwords, 'API' keys,
etc., in R packages, using public key cryptography.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/internals.md
%doc %{rlibdir}/%{packname}/README.markdown
%doc %{rlibdir}/%{packname}/README.Rmd
%doc %{rlibdir}/%{packname}/user_keys
%doc %{rlibdir}/%{packname}/vignette_child
%{rlibdir}/%{packname}/INDEX
