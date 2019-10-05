%global packname  GWASinspector
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Comprehensive and Easy to Use Quality Control of GWAS Results

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-tools >= 3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-hash >= 2.2
BuildRequires:    R-CRAN-futile.logger >= 1.4
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-knitr >= 1.1
BuildRequires:    R-CRAN-rmarkdown >= 0.9
BuildRequires:    R-CRAN-kableExtra >= 0.8
BuildRequires:    R-CRAN-ini >= 0.3
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-tools >= 3.0
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-hash >= 2.2
Requires:         R-CRAN-futile.logger >= 1.4
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-knitr >= 1.1
Requires:         R-CRAN-rmarkdown >= 0.9
Requires:         R-CRAN-kableExtra >= 0.8
Requires:         R-CRAN-ini >= 0.3
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-RSQLite 

%description
When evaluating the results of a genome-wide association study (GWAS), it
is important to perform a quality control to ensure that the results are
valid, complete, correctly formatted, and, in case of meta-analysis,
consistent with other studies that have applied the same analysis. This
package was developed to facilitate and streamline this process and
provide the user with a comprehensive report.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rmd
%{rlibdir}/%{packname}/INDEX
