%global packname  comperank
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Ranking Methods for Competition Results

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-dplyr >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-comperes >= 0.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 0.6.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-comperes >= 0.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 

%description
Compute ranking and rating based on competition results. Methods of
different nature are implemented: with fixed Head-to-Head structure, with
variable Head-to-Head structure and with iterative nature. All algorithms
are taken from the book 'Who’s #1?: The science of rating and ranking' by
Amy N. Langville and Carl D. Meyer (2012, ISBN:978-0-691-15422-0).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
