%global packname  fda
%global packver   2.4.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.8.1
Release:          1%{?dist}
Summary:          Functional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
Requires:         R-splines 
Requires:         R-Matrix 
Requires:         R-graphics 

%description
These functions were developed to support functional data analysis as
described in Ramsay, J. O. and Silverman, B. W. (2005) Functional Data
Analysis. New York: Springer.  They were ported from earlier versions in
Matlab and S-PLUS.  An introduction appears in Ramsay, J. O., Hooker,
Giles, and Graves, Spencer (2009) Functional Data Analysis with R and
Matlab (Springer). The package includes data sets and script files working
many examples including all but one of the 76 figures in this latter book.
Matlab versions of the code and sample analyses are no longer distributed
through CRAN, as they were when the book was published.  For those, ftp
from <http://www.psych.mcgill.ca/misc/fda/downloads/FDAfuns/> There you
find a set of .zip files containing the functions and sample analyses, as
well as two .txt files giving instructions for installation and some
additional information. The changes from Version 2.4.1 are fixes of bugs
in density.fd and removal of functions create.polynomial.basis,
polynompen, and polynomial. These were deleted because the monomial basis
does the same thing and because there were errors in the code.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Matlab
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
