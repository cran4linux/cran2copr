%global __brp_check_rpaths %{nil}
%global packname  autota
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Auto TA

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-base64enc 

%description
Auto TA (teaching assistant) provides contextual help for common error
messages. For example, if you get a syntax error (e.g. "unexpected string
constant"), the Auto TA will explain what the string constant is, why it
was unexpected, and possible ways to fix it.

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
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/ui
%{rlibdir}/%{packname}/INDEX
