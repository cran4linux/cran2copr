%global packname  HSAUR3
%global packver   1.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}
Summary:          A Handbook of Statistical Analyses Using R (3rd Edition)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-tools 
Requires:         R-tools 

%description
Functions, data sets, analyses and examples from the third edition of the
book ''A Handbook of Statistical Analyses Using R'' (Torsten Hothorn and
Brian S. Everitt, Chapman & Hall/CRC, 2014). The first chapter of the
book, which is entitled ''An Introduction to R'', is completely included
in this package, for all other chapters, a vignette containing all data
analyses is available. In addition, Sweave source code for slides of
selected chapters is included in this package (see HSAUR3/inst/slides).
The publishers web page is
'<http://www.crcpress.com/product/isbn/9781482204582>'.

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
%doc %{rlibdir}/%{packname}/cache
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/LaTeXBibTeX
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/rawdata
%doc %{rlibdir}/%{packname}/slides
%{rlibdir}/%{packname}/INDEX
