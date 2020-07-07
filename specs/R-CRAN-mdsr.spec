%global packname  mdsr
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          3%{?dist}
Summary:          Complement to 'Modern Data Science with R'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-babynames 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mosaic 
BuildRequires:    R-CRAN-RMySQL 
Requires:         R-CRAN-babynames 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mosaic 
Requires:         R-CRAN-RMySQL 

%description
A complement to *Modern Data Science with R* (ISBN: 978-1498724487,
publisher URL:
<https://www.crcpress.com/Modern-Data-Science-with-R/Baumer-Kaplan-Horton/p/book/9781498724487>).
This package contains all of the data and code necessary to complete
exercises and reproduce examples from the text. It also facilitates
connections to the SQL database server used in the book.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
