%global packname  blogdown
%global packver   0.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17
Release:          1%{?dist}
Summary:          Create Blogs and Websites with R Markdown

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         hugo
Requires:         pandoc
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.19
BuildRequires:    R-CRAN-httpuv >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.25
BuildRequires:    R-CRAN-rmarkdown >= 1.16
BuildRequires:    R-CRAN-servr >= 0.15
BuildRequires:    R-CRAN-bookdown >= 0.14
BuildRequires:    R-CRAN-xfun >= 0.10
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-yaml >= 2.1.19
Requires:         R-CRAN-httpuv >= 1.4.0
Requires:         R-CRAN-knitr >= 1.25
Requires:         R-CRAN-rmarkdown >= 1.16
Requires:         R-CRAN-servr >= 0.15
Requires:         R-CRAN-bookdown >= 0.14
Requires:         R-CRAN-xfun >= 0.10
Requires:         R-CRAN-htmltools 

%description
Write blog posts and web pages in R Markdown. This package supports the
static site generator 'Hugo' (<https://gohugo.io>) best, and it also
supports 'Jekyll' (<http://jekyllrb.com>) and 'Hexo' (<https://hexo.io>).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/resources
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
