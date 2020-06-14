%global packname  homologene
%global packver   1.4.68.19.3.27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.68.19.3.27
Release:          2%{?dist}
Summary:          Quick Access to Homologene and Gene Annotation Updates

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.8.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-R.utils >= 2.8.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-purrr >= 0.2.5

%description
A wrapper for the homologene database by the National Center for
Biotechnology Information ('NCBI'). It allows searching for gene homologs
across species. Data in this package can be found at
<ftp://ftp.ncbi.nih.gov/pub/HomoloGene/build68/>. The package also
includes an updated version of the homologene database where gene
identifiers and symbols are replaced with their latest (at the time of
submission) version and functions to fetch latest annotation data to keep
updated.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
