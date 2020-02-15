%global packname  rcosmo
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Cosmic Microwave Background Data Analysis

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-FITSio >= 2.1.0
BuildRequires:    R-CRAN-geoR >= 1.7.5.2.1
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-nnls >= 1.4
BuildRequires:    R-CRAN-entropy >= 1.2.1
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-rgl >= 0.99.16
BuildRequires:    R-CRAN-mmap >= 0.6.17
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-FITSio >= 2.1.0
Requires:         R-CRAN-geoR >= 1.7.5.2.1
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-nnls >= 1.4
Requires:         R-CRAN-entropy >= 1.2.1
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-rgl >= 0.99.16
Requires:         R-CRAN-mmap >= 0.6.17
Requires:         R-CRAN-Rcpp >= 0.12.11

%description
Handling and Analysing Spherical, HEALPix and Cosmic Microwave Background
data on a HEALPix grid.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
