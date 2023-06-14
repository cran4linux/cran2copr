%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  disclosuR
%global packver   0.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Text Conversion from Nexis Uni PDFs to R Data Frames

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-qdap 
BuildRequires:    R-CRAN-SentimentAnalysis 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-syuzhet 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-qdap 
Requires:         R-CRAN-SentimentAnalysis 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-syuzhet 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-tm 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Transform 'newswire' and earnings call transcripts as PDF obtained from
'Nexis Uni' to R data frames. Various 'newswires' and 'FairDisclosure'
earnings call formats are supported. Further, users can apply several
pre-defined dictionaries on the data based on Graffin et al.
(2016)<doi:10.5465/amj.2013.0288> and Gamache et al.
(2015)<doi:10.5465/amj.2013.0377>.

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
