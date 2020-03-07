%global packname  deepdep
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Visualise and Explore the Deep Dependencies of R Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cranlogs 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-graphlayouts 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-cranlogs 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-graphlayouts 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-scales 

%description
Provides the tools for exploration of package dependencies. Main deepdep()
function allows to acquire deep dependencies of any package and plot them
in an elegant way. It also adds some popularity measures for the packages
e.g. in the form of download count through the 'cranlogs' package. Uses
the CRAN metadata database <http://crandb.r-pkg.org> and Bioconductor
metadata <http://bioconductor.org>. Other data acquire functions are:
get_dependencies(), get_downloads() and get_description(). The
deepdep_shiny() function runs shiny application that helps to produce nice
'deepdep' plot.

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
%doc %{rlibdir}/%{packname}/shiny_app
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
