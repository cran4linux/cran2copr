%global __brp_check_rpaths %{nil}
%global packname  RWebLogo
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          plotting custom sequence logos

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         ghostscript
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-findpython 
Requires:         R-CRAN-findpython 

%description
RWebLogo is a wrapper for the WebLogo python package that allows
generating of customised sequence logos. Sequence logos are graphical
representations of the sequence conservation of nucleotides (in a strand
of DNA/RNA) or amino acids (in protein sequences). Each logo consists of
stacks of symbols, one stack for each position in the sequence. The
overall height of the stack indicates the sequence conservation at that
position, while the height of symbols within the stack indicates the
relative frequency of each amino or nucleic acid at that position. In
general, a sequence logo provides a richer and more precise description
of, for example, a binding site, than would a consensus sequence.

%prep
%setup -q -c -n %{packname}
find %{packname}/inst -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
