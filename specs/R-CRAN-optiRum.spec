%global packname  optiRum
%global packver   0.40.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.40.1
Release:          1%{?dist}
Summary:          Financial Functions & More

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-AUC 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-AUC 
Requires:         R-grid 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-XML 

%description
This fills the gaps credit analysts and loan modellers at Optimum Credit
identify in the existing R code body. It allows for the production of
documentation with less coding, replicates a number of Microsoft Excel
functions useful for modelling loans (without rounding), and other helpful
functions for producing charts and tables.  It also has some additional
scales for use, including a GBP scale.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
