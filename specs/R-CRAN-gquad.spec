%global packname  gquad
%global packver   2.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Prediction of G Quadruplexes and Other Non-B DNA Motifs

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 4.0
BuildRequires:    R-CRAN-seqinr >= 3.3.3
Requires:         R-CRAN-ape >= 4.0
Requires:         R-CRAN-seqinr >= 3.3.3

%description
Genomic biology is not limited to the confines of the canonical B- forming
DNA duplex, but includes over ten different types of other secondary
structures that are collectively termed non-B DNA structures. Of these
non-B DNA structures, the G-quadruplexes are highly stable four-stranded
structures that are recognized by distinct subsets of nuclear factors.
This package provide functions for predicting intramolecular G
quadruplexes. In addition, functions for predicting other intramolecular
nonB DNA structures are included.

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
%{rlibdir}/%{packname}/INDEX
