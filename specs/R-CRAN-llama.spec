%global packname  llama
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          2%{?dist}%{?buildtag}
Summary:          Leveraging Learning to Automatically Manage Algorithms

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr >= 2.5
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-mlr >= 2.5
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-plyr 

%description
Provides functionality to train and evaluate algorithm selection models
for portfolios.

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

%files
%{rlibdir}/%{packname}
