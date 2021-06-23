%global __brp_check_rpaths %{nil}
%global packname  farff
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Faster 'ARFF' File Reader and Writer

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-checkmate >= 1.8.0
BuildRequires:    R-CRAN-readr >= 1.0.0
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-checkmate >= 1.8.0
Requires:         R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-stringi 

%description
Reads and writes 'ARFF' files. 'ARFF' (Attribute-Relation File Format)
files are like 'CSV' files, with a little bit of added meta information in
a header and standardized NA values. They are quite often used for machine
learning data sets and were introduced for the 'WEKA' machine learning
'Java' toolbox. See
<https://waikato.github.io/weka-wiki/formats_and_processing/arff_stable/>
for further info on 'ARFF' and for <http://www.cs.waikato.ac.nz/ml/weka/>
for more info on 'WEKA'. 'farff' gets rid of the 'Java' dependency that
'RWeka' enforces, and it is at least a faster reader (for bigger files).
It uses 'readr' as parser back-end for the data section of the 'ARFF'
file. Consistency with 'RWeka' is tested on 'Github' and 'Travis CI' with
hundreds of 'ARFF' files from 'OpenML'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
