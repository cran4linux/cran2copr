%global packname  RmecabKo
%global packver   0.1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6.2
Release:          2%{?dist}
Summary:          An 'Rcpp' Interface for Eunjeon Project

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    mecab-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringr 

%description
An 'Rcpp' interface for Eunjeon project <http://eunjeon.blogspot.com/>.
The 'mecab-ko' and 'mecab-ko-dic' is based on a C++ library, and
part-of-speech tagging with them is useful when the spacing of source
Korean text is not correct. This package provides part-of-speech tagging
and tokenization function for Korean text.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
