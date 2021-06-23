%global __brp_check_rpaths %{nil}
%global packname  RecordLinkage
%global packver   0.4-12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.12.1
Release:          1%{?dist}%{?buildtag}
Summary:          Record Linkage Functions for Linking and Deduplicating Data Sets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.7.8
BuildRequires:    R-CRAN-RSQLite >= 1.0.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-ada 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-methods 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-data.table >= 1.7.8
Requires:         R-CRAN-RSQLite >= 1.0.0
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-e1071 
Requires:         R-rpart 
Requires:         R-CRAN-ada 
Requires:         R-CRAN-ipred 
Requires:         R-stats 
Requires:         R-CRAN-evd 
Requires:         R-methods 
Requires:         R-nnet 
Requires:         R-CRAN-xtable 

%description
Provides functions for linking and deduplicating data sets. Methods based
on a stochastic approach are implemented as well as classification
algorithms from the machine learning domain. For details, see our paper
"The RecordLinkage Package: Detecting Errors in Data" Sariyar M / Borg A
(2010) <doi:10.32614/RJ-2010-017>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
