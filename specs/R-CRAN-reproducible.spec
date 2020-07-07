%global packname  reproducible
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          A Set of Tools that Enhance Reproducibility Beyond PackageManagement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fastdigest 
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qs 
BuildRequires:    R-CRAN-quickPlot 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-versions 
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-backports 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fastdigest 
Requires:         R-CRAN-fpCompare 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-qs 
Requires:         R-CRAN-quickPlot 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-testthat 
Requires:         R-tools 
Requires:         R-CRAN-usethis 
Requires:         R-utils 
Requires:         R-CRAN-versions 

%description
Collection of high-level, robust, machine- and OS-independent tools for
making deeply reproducible and reusable content in R. The three workhorse
functions are Cache, prepInputs, and Require; these allow for nested
caching, robust to environments, and objects with environments (like
functions), and data retrieval and processing, and package handling in
continuous workflow environments. In all cases, efforts are made to make
the first and subsequent calls of functions have the same result, but
vastly faster at subsequent times by way of checksums and digesting.
Several features are still under active development, including cloud
storage of cached objects, allowing for sharing between users.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
