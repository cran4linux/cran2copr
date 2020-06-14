%global packname  staplr
%global packver   2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.0
Release:          2%{?dist}
Summary:          A Toolkit for PDF Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glue 
Requires:         R-tcltk 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glue 

%description
Provides function to manipulate PDF files: fill out PDF forms; merge
multiple PDF files into one; remove selected pages from a file; rename
multiple files in a directory; rotate entire pdf document; rotate selected
pages of a pdf file; Select pages from a file; splits single input PDF
document into individual pages; splits single input PDF document into
parts from given points.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/testForm.pdf
%{rlibdir}/%{packname}/INDEX
