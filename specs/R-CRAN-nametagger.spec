%global packname  nametagger
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Named Entity Recognition in Texts using 'NameTag'

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-udpipe >= 0.8.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-utils 
Requires:         R-CRAN-udpipe >= 0.8.1
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-utils 

%description
Wraps the 'nametag' library <https://github.com/ufal/nametag>, allowing
users to find and extract entities (names, persons, locations, addresses,
...) in raw text and build your own entity recognition models. Based on a
maximum entropy Markov model which is described in Strakova J., Straka M.
and Hajic J. (2013)
<http://ufal.mff.cuni.cz/~straka/papers/2013-tsd_ner.pdf>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
