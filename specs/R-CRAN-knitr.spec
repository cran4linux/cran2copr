%global packname  knitr
%global packver   1.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.29
Release:          2%{?dist}
Summary:          A General-Purpose Package for Dynamic Report Generation in R

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
Requires:         pandoc-citeproc
BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.19
BuildRequires:    R-CRAN-stringr >= 0.6
BuildRequires:    R-CRAN-xfun >= 0.15
BuildRequires:    R-CRAN-evaluate >= 0.10
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
Requires:         R-CRAN-yaml >= 2.1.19
Requires:         R-CRAN-stringr >= 0.6
Requires:         R-CRAN-xfun >= 0.15
Requires:         R-CRAN-evaluate >= 0.10
Requires:         R-CRAN-highr 
Requires:         R-CRAN-markdown 
Requires:         R-methods 
Requires:         R-tools 

%description
Provides a general-purpose tool for dynamic report generation in R using
Literate Programming techniques.

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
