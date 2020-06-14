%global packname  RWsearch
%global packver   4.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.8.0
Release:          2%{?dist}
Summary:          Lazy Search in R Packages, Task Views, CRAN, the Web. All-in-OneDownload

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-latexpdf 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-sig 
BuildRequires:    R-CRAN-sos 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-latexpdf 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-sig 
Requires:         R-CRAN-sos 
Requires:         R-CRAN-XML 

%description
Search by keywords in R packages, task views, CRAN, the web and display
the results in the console or in txt, html or pdf files. Download the
whole documentation of packages (html index, pdf manual, vignettes, source
code, etc) with a single instruction. Visualize the package dependencies
and CRAN checks. Explore CRAN archive. Use the above functions for task
view maintenance. Use quick links and 70 web search engines to explore the
web. A lazy evaluation of non-standard content is available throughout the
package and eases the use of many functions.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/aabb
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
