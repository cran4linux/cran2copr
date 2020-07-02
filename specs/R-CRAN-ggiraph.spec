%global packname  ggiraph
%global packver   0.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.8
Release:          1%{?dist}
Summary:          Make 'ggplot2' Graphics Interactive

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-htmlwidgets >= 0.6
BuildRequires:    R-CRAN-gdtools >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-htmlwidgets >= 0.6
Requires:         R-CRAN-gdtools >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-uuid 

%description
Create interactive 'ggplot2' graphics using 'htmlwidgets'.

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
