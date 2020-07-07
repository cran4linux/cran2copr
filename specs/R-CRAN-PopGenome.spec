%global packname  PopGenome
%global packver   2.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.5
Release:          3%{?dist}
Summary:          An Efficient Swiss Army Knife for Population Genomic Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zlib-devel
Requires:         zlib
BuildRequires:    R-devel >= 2.14.2
Requires:         R-core >= 2.14.2
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-methods 
Requires:         R-CRAN-ff 
Requires:         R-methods 

%description
Provides efficient tools for population genomics data analysis, able to
process individual loci, large sets of loci, or whole genomes. PopGenome
<DOI:10.1093/molbev/msu136> not only implements a wide range of population
genetics statistics, but also facilitates the easy implementation of new
algorithms by other researchers. PopGenome is optimized for speed via the
seamless integration of C code.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
