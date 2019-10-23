%global packname  tutorial
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Convert R Markdown Files to DataCamp Light HTML Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-base64enc 

%description
DataCamp Light (<https://github.com/datacamp/datacamp-light>) is a
light-weight implementation of the DataCamp UI, that allows you to embed
interactive exercises inside HTML documents. The tutorial package makes it
easy to create these HTML files from R Markdown files. An extension to
knitr, tutorial detects appropriately formatted code chunks and replaces
them with DataCamp Light readable chunks in the resulting HTML file.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example.Rmd
%{rlibdir}/%{packname}/INDEX
