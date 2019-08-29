%global packname  DataPackageR
%global packver   0.15.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.7
Release:          1%{?dist}
Summary:          Construct Reproducible Analytic Data Sets as R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc >= 1.12.3
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 >= 6.0.1
BuildRequires:    R-CRAN-devtools >= 1.12.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-roxygen2 >= 6.0.1
Requires:         R-CRAN-devtools >= 1.12.0
Requires:         R-CRAN-digest 
Requires:         R-CRAN-knitr 
Requires:         R-utils 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-crayon 

%description
A framework to help construct R data packages in a reproducible manner.
Potentially time consuming processing of raw data sets into analysis ready
data sets is done in a reproducible manner and decoupled from the usual R
CMD build process so that data sets can be processed into R objects in the
data package and the data package can then be shared, built, and installed
by others without the need to repeat computationally costly data
processing. The package maintains data provenance by turning the data
processing scripts into package vignettes, as well as enforcing
documentation and version checking of included data objects. Data packages
can be version controlled in github, and used to share data for
manuscripts, collaboration and general reproducibility.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
