%global packname  latexpdf
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Convert Tables to PDF or PNG

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Converts table-like objects to stand-alone PDF or PNG. Can be used to
embed tables and arbitrary content in PDF or Word documents. Provides a
low-level R interface for creating 'LaTeX' code, e.g. command() and a
high-level interface for creating PDF documents, e.g. as.pdf.data.frame().
Extensive customization is available via mid-level functions, e.g.
as.tabular(). See also 'package?latexpdf'. Support for PNG is
experimental; see 'as.png.data.frame'. Adapted from 'metrumrg'
<http://r-forge.r-project.org/R/?group_id=1215>. Requires a compatible
installation of 'pdflatex', e.g. <https://miktex.org/>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
