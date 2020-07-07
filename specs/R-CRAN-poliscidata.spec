%global packname  poliscidata
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}
Summary:          Datasets and Functions Featured in Pollock and Edwards, an RCompanion to Essentials of Political Analysis, Second Edition

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-descr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-abind 
Requires:         R-methods 
Requires:         R-CRAN-descr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-car 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-abind 

%description
Bundles the datasets and functions used in the textbook by Philip Pollock
and Barry Edwards, an R Companion to Essentials of Political Analysis,
Second Edition.

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
