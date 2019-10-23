%global packname  ProgGUIinR
%global packver   0.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          support package for "Programming Graphical User Interfaces in R"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-svMisc 
BuildRequires:    R-MASS 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-svMisc 
Requires:         R-MASS 

%description
sample code, appendices and functions for the text Programming GUIs in R

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Examples
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/qt
%doc %{rlibdir}/%{packname}/resources
%doc %{rlibdir}/%{packname}/source-code-by-part
%{rlibdir}/%{packname}/INDEX
