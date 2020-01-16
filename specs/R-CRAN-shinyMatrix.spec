%global packname  shinyMatrix
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Shiny Matrix Input Field

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 

%description
Implements a custom matrix input field.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/appCopy
%doc %{rlibdir}/%{packname}/appCustom
%doc %{rlibdir}/%{packname}/appEmpty
%doc %{rlibdir}/%{packname}/appExtend
%doc %{rlibdir}/%{packname}/appExtendNoNames
%doc %{rlibdir}/%{packname}/appRownames
%doc %{rlibdir}/%{packname}/appUpdate
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
