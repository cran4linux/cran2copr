%global packname  CEDARS
%global packver   1.90
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.90
Release:          1%{?dist}%{?buildtag}
Summary:          Simple and Efficient Pipeline for Electronic Health Record Annotation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mongolite 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-udpipe 
BuildRequires:    R-utils 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mongolite 
Requires:         R-parallel 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-udpipe 
Requires:         R-utils 

%description
Streamlined annotation pipeline for collection and aggregation of
time-to-event data in retrospective clinical studies. 'CEDARS' aims to
systematize and accelerate the review of electronic health record (EHR)
corpora. It accomplishes those goals by deploying natural language
processing as a tool to assist detection and characterization of clinical
events by human abstractors. The online user manual presents the necessary
steps to install 'CEDARS', process EHR corpora and obtain clinical event
dates: <https://cedars.io>.

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
