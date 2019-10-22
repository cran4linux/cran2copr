%global packname  nima
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Nima Hejazi's R Toolbox

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-ProjectTemplate 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grid 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-gtools 
Requires:         R-survival 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-ProjectTemplate 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plyr 
Requires:         R-grid 

%description
Miscellaneous R functions developed over the course of statistical
research and scientific computing. These include, for example, utilities
that supplement existing idiosyncrasies of the R language, extend existing
plotting functionality and aesthetics, provide alternative presentations
of matrix decompositions, and extend access to command line tools and
systems-level information.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
