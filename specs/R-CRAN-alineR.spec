%global packname  alineR
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Alignment of Phonetic Sequences Using the 'ALINE' Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Functions are provided to calculate the 'ALINE' Distance between words as
per (Kondrak 2000) and (Downey, Hallmark, Cox, Norquest, & Lansing, 2008,
<doi:10.1080/09296170802326681>). The score is based on phonetic features
represented using the Unicode-compliant International Phonetic Alphabet
(IPA). Parameterized features weights are used to determine the optimal
alignment and functions are provided to estimate optimum values using a
genetic algorithm and supervised learning. See (Downey, Sun, and Norquest
2017, <https://journal.r-project.org/archive/2017/RJ-2017-005/index.html>.

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
%{rlibdir}/%{packname}/libs
