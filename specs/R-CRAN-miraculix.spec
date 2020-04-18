%global packname  miraculix
%global packver   0.9.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.20
Release:          1%{?dist}
Summary:          Algebraic and Statistical Functions for Genetics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-RandomFieldsUtils >= 0.5
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-RandomFieldsUtils >= 0.5
Requires:         R-methods 
Requires:         R-graphics 

%description
This is a collection of fast tools for application in quantitative
genetics. For instance, the SNP matrix can be stored in a minimum of
memory and the calculation of the genomic relationship matrix is based on
a rapid algorithm. It also contains the window scanning approach by
Kabluchko and Spodarev (2009), <doi:10.1239/aap/1240319575> to detect
anomalous genomic areas <doi:10.1186/s12864-018-5009-y>. Furthermore, the
package is used in the Modular Breeding Program Simulator (MoBPS,
<https://github.com/tpook92/MoBPS>, <http://www.mobps.de/>). The tools are
based on SIMD (Single Instruction Multiple Data,
<https://en.wikipedia.org/wiki/SIMD>) and OMP (Open Multi-Processing,
<https://de.wikipedia.org/wiki/OpenMP>).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
