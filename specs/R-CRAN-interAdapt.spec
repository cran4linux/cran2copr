%global packname  interAdapt
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          interAdapt

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-knitcitations 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-knitcitations 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-knitr 

%description
A shiny application for designing adaptive clinical trials. For more
details, see: http://arxiv.org/abs/1404.0734

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/csv
%doc %{rlibdir}/%{packname}/shinyInterAdaptApp
%{rlibdir}/%{packname}/INDEX
