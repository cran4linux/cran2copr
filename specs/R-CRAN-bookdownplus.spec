%global packname  bookdownplus
%global packver   1.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.8
Release:          2%{?dist}
Summary:          Generate Assorted Books and Documents with R 'bookdown' Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bookdown >= 0.3
BuildRequires:    R-CRAN-xaringan 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-bookdown >= 0.3
Requires:         R-CRAN-xaringan 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-knitr 

%description
A collection and selector of R 'bookdown' templates. 'bookdownplus' helps
you write academic journal articles, guitar books, chemical equations,
mails, calendars, and diaries. R 'bookdownplus' extends the features of
'bookdown', and simplifies the procedure. Users only have to choose a
template, clarify the book title and author name, and then focus on
writing the text. No need to struggle in 'YAML' and 'LaTeX'.

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
%doc %{rlibdir}/%{packname}/bib
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/proj
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/yml
%{rlibdir}/%{packname}/INDEX
