%global packname  dash
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          An Interface to the 'dash' Ecosystem for Authoring Reactive WebApplications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-reqres >= 0.2.3
BuildRequires:    R-CRAN-fiery > 1.0.0
BuildRequires:    R-CRAN-routr > 0.2.0
BuildRequires:    R-CRAN-dashTable == 4.7.0
BuildRequires:    R-CRAN-dashCoreComponents == 1.10.0
BuildRequires:    R-CRAN-dashHtmlComponents == 1.0.3
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-brotli 
Requires:         R-CRAN-reqres >= 0.2.3
Requires:         R-CRAN-fiery > 1.0.0
Requires:         R-CRAN-routr > 0.2.0
Requires:         R-CRAN-dashTable == 4.7.0
Requires:         R-CRAN-dashCoreComponents == 1.10.0
Requires:         R-CRAN-dashHtmlComponents == 1.0.3
Requires:         R-CRAN-R6 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-brotli 

%description
A framework for building analytical web applications, 'dash' offers a
pleasant and productive development experience. No JavaScript required.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/lib
%{rlibdir}/%{packname}/INDEX
