%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tableParser
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parse Tabled Content to Text Vector and Extract Statistical Standard Results

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-JATSdecoder 
BuildRequires:    R-CRAN-tabulapdf 
Requires:         R-utils 
Requires:         R-CRAN-JATSdecoder 
Requires:         R-CRAN-tabulapdf 

%description
Features include the ability to extract tabled content from
NISO-JATS-coded XML, any native HTML or HML file, DOCX, and PDF documents,
and then collapse it into a text format that is readable by humans by
mimicking the actions of a screen reader. As tables within PDF documents
are extracted with the 'tabulapdf' package, and the table captions and
footnotes cannot be extracted, the results on tables within PDF documents
have to be considered less precise. The function table2matrix() returns a
list of the tables within a document as character matrices. table2text()
collapses the matrix content into a list of character strings by imitating
the behavior of a screen reader. The textual representation of characters
and numbers can be unified with unifyMatrix() before parsing. The function
table2stats() extracts the tabled statistical test results from the
collapsed text with the function standardStats() from the 'JATSdecoder'
package and, if activated, checks the reported and coded p-values for
consistency. Due to the great variability and potential complexity of
table structures, parsing accuracy may vary.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
