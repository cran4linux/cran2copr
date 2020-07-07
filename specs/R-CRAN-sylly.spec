%global packname  sylly
%global packver   0.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Hyphenation and Syllable Counting for Text Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Provides the hyphenation algorithm used for 'TeX'/'LaTeX' and similar
software, as proposed by Liang (1983, <https://tug.org/docs/liang/>).
Mainly contains the function hyphen() to be used for hyphenation/syllable
counting of text objects. It was originally developed for and part of the
'koRpus' package, but later released as a separate package so it's lighter
to have this particular functionality available for other packages.
Support for various languages needs be added on-the-fly or by plugin
packages (<https://undocumeantit.github.io/repos>); this package does not
include any language specific data. Due to some restrictions on CRAN, the
full package sources are only available from the project homepage. To ask
for help, report bugs, request features, or discuss the development of the
package, please subscribe to the koRpus-dev mailing list
(<http://korpusml.reaktanz.de>).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
