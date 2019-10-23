%global packname  fgeo
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Analyze Forest Diversity and Dynamics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-fgeo.tool >= 1.2.4
BuildRequires:    R-CRAN-fgeo.plot >= 1.1.6
BuildRequires:    R-CRAN-fgeo.x >= 1.1.3
BuildRequires:    R-CRAN-fgeo.analyze >= 1.1.10
BuildRequires:    R-CRAN-cli >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-rstudioapi >= 0.10
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-fgeo.tool >= 1.2.4
Requires:         R-CRAN-fgeo.plot >= 1.1.6
Requires:         R-CRAN-fgeo.x >= 1.1.3
Requires:         R-CRAN-fgeo.analyze >= 1.1.10
Requires:         R-CRAN-cli >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-rstudioapi >= 0.10
Requires:         R-utils 

%description
To help you access, transform, analyze, and visualize ForestGEO data, we
developed a collection of R packages
(<https://forestgeo.github.io/fgeo/>). This package, in particular, helps
you to install and load the entire package-collection with a single R
command, and provides convenient ways to find relevant documentation. Most
commonly, you should not worry about the individual packages that make up
the package-collection as you can access all features via this package. To
learn more about ForestGEO visit <http://www.forestgeo.si.edu/>.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
