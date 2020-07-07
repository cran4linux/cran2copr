%global packname  recmap
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}
Summary:          Compute the Rectangular Statistical Cartogram

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-GA >= 3.1
BuildRequires:    R-CRAN-sp >= 1.3
BuildRequires:    R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-GA >= 3.1
Requires:         R-CRAN-sp >= 1.3
Requires:         R-CRAN-Rcpp >= 1.0

%description
Provides an interface and a C++ implementation of the RecMap MP2
construction heuristic (Panse C. (2018) <doi:10.18637/jss.v086.c01>). This
algorithm draws maps according to a given statistical value (e.g.,
election results, population or epidemiological data). The basic idea of
the RecMap algorithm is that each map region (e.g., different countries)
is represented by a rectangle. The area of each rectangle represents the
statistical value given as input (maintain zero cartographic error).
Documentation about the usage of the recmap algorithm is provided by a
vignette included in this package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
