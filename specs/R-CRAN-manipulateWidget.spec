%global packname  manipulateWidget
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          1%{?dist}
Summary:          Add Even More Interactivity to Interactive Charts

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-grDevices 
BuildRequires:    R-codetools 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-CRAN-base64enc 
Requires:         R-grDevices 
Requires:         R-codetools 
Requires:         R-CRAN-webshot 

%description
Like package 'manipulate' does for static graphics, this package helps to
easily add controls like sliders, pickers, checkboxes, etc. that can be
used to modify the input data or the parameters of an interactive chart
created with package 'htmlwidgets'.

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
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/lib
%doc %{rlibdir}/%{packname}/manipulate_widget
%{rlibdir}/%{packname}/INDEX
