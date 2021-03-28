%global packname  cat2cat
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping of a Categorical Variable in a Panel Dataset

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-assertthat 

%description
There are offered automatic methods to map a categorical variable
according to a specific encoding across different time points. The main
rule is to replicate the observation if it could be assign to a few
categories. Then using simple frequencies or statistical methods to
approximate probabilities of being assign to each of them. This algorithm
was invented and implemented in the paper by (Nasinski, Majchrowska and
Broniatowska (2020) <doi:10.24425/cejeme.2020.134747>).

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
