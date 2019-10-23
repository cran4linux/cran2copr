%global packname  corregp
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Functions and Methods for Correspondence Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-rgl 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-gplots 
Requires:         R-utils 

%description
A collection of tools for correspondence regression, i.e. the
correspondence analysis of the crosstabulation of a categorical variable Y
in function of another one X, where X can in turn be made up of the
combination of various categorical variables. Consequently, correspondence
regression can be used to analyze the effects for a polytomous or
multinomial outcome variable.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
