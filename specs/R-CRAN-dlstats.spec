%global packname  dlstats
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Download Stats of R Packages

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-utils 

%description
Monthly download stats of 'CRAN' and 'Bioconductor' packages. Download
stats of 'CRAN' packages is from the 'RStudio' 'CRAN mirror', see
<http://cranlogs.r-pkg.org>. 'Bioconductor' package download stats is at
<https://bioconductor.org/packages/stats/>.

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
%doc %{rlibdir}/%{packname}/biocApp
%doc %{rlibdir}/%{packname}/cranApp
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
