%global packname  cnum
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Chinese Numerals Processing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Rcpp 

%description
Chinese numerals processing in R, such as conversion between Chinese
numerals and Arabic numerals as well as detection and extraction of
Chinese numerals in character objects and string. This package supports
the casual scale naming system and the respective SI prefix systems used
in mainland China and Taiwan: "China Statutory Measurement Units" State
Administration for Market Regulation (2019)
<http://gkml.samr.gov.cn/nsjg/jls/201902/t20190225_291134.html> "Names,
Definitions and Symbols of the Legal Units of Measurement and the Decimal
Multiples and Submultiples" Ministry of Economic Affairs (2019)
<https://gazette.nat.gov.tw/egFront/detail.do?metaid=108965>.

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
