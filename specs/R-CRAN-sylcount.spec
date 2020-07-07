%global packname  sylcount
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          Syllable Counting and Readability Measurements

License:          BSD 2-clause License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
An English language syllable counter, plus readability score measure-er.
For readability, we support 'Flesch' Reading Ease and 'Flesch-Kincaid'
Grade Level ('Kincaid' 'et al'. 1975)
<https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1055&context=istlibrary>,
Automated Readability Index ('Senter' and Smith 1967)
<http://www.dtic.mil/cgi-bin/GetTRDoc?AD=AD0667273>, Simple Measure of
Gobbledygook (McLaughlin 1969)
<https://www.semanticscholar.org/paper/SMOG-Grading-A-New-Readability-Formula.-Laughlin/5fccb74c14769762b3de010c5e8a1a7ce700d17a>,
and 'Coleman-Liau' (Coleman and 'Liau' 1975) <doi:10.1037/h0076540>. The
package has been carefully optimized and should be very efficient, both in
terms of run time performance and memory consumption. The main methods are
'vectorized' by document, and scores for multiple documents are computed
in parallel via 'OpenMP'.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
