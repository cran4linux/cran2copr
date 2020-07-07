%global packname  robustrao
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}
Summary:          An Extended Rao-Stirling Diversity Index to Handle Missing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog >= 1.5.5
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-gmp >= 0.5.12
BuildRequires:    R-CRAN-iterpc >= 0.3.0
Requires:         R-CRAN-quadprog >= 1.5.5
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-gmp >= 0.5.12
Requires:         R-CRAN-iterpc >= 0.3.0

%description
A collection of functions to compute the Rao-Stirling diversity index
(Porter and Rafols, 2009) <DOI:10.1007/s11192-008-2197-2> and its
extension to acknowledge missing data (i.e., uncategorized references) by
calculating its interval of uncertainty using mathematical optimization as
proposed in Calatrava et al. (2016) <DOI:10.1007/s11192-016-1842-4>. The
Rao-Stirling diversity index is a well-established bibliometric indicator
to measure the interdisciplinarity of scientific publications. Apart from
the obligatory dataset of publications with their respective references
and a taxonomy of disciplines that categorizes references as well as a
measure of similarity between the disciplines, the Rao-Stirling diversity
index requires a complete categorization of all references of a
publication into disciplines. Thus, it fails for a incomplete
categorization; in this case, the robust extension has to be used, which
encodes the uncertainty caused by missing bibliographic data as an
uncertainty interval. Classification / ACM - 2012: Information systems ~
Similarity measures, Theory of computation ~ Quadratic programming,
Applied computing ~ Digital libraries and archives.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
