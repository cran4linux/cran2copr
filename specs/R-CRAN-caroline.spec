%global packname  caroline
%global packver   0.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.6
Release:          2%{?dist}
Summary:          A Collection of Database, Data Structure, Visualization, andUtility Functions for R

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch

%description
The caroline R library contains dozens of functions useful for: database
migration (dbWriteTable2), database style joins & aggregation (nerge,
groupBy & bestBy), data structure conversion (nv, tab2df), legend table
making (sstable & leghead), plot annotation (labsegs & mvlabs), data
visualization (violins, pies & raPlot), character string manipulation (m &
pad), file I/O (write.delim), batch scripting and more.  The package's
greatest contributions lie in the database style merge, aggregation and
interface functions as well as in it's extensive use and propagation of
row, column and vector names in most functions.

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
