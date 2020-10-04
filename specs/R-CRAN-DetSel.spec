%global packname  DetSel
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          A Computer Program to Detect Markers Responding to Selection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildRequires:    R-CRAN-ash 
Requires:         R-CRAN-ash 

%description
In the new era of population genomics, surveys of genetic polymorphism
("genome scans") offer the opportunity to distinguish locus-specific from
genome wide effects at many loci. Identifying presumably neutral regions
of the genome that are assumed to be influenced by genome-wide effects
only, and excluding presumably selected regions, is therefore critical to
infer population demography and phylogenetic history reliably. Conversely,
detecting locus-specific effects may help identify those genes that have
been, or still are, targeted by natural selection. The software package
DetSel has been developed to identify markers that show deviation from
neutral expectation in pairwise comparisons of diverging populations.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data.dat
%{rlibdir}/%{packname}/data.gen
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
