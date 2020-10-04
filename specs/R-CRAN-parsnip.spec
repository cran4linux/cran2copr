%global packname  parsnip
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Common API to Modeling and Analysis Functions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-vctrs >= 0.2.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-globals 
BuildRequires:    R-CRAN-prettyunits 
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-vctrs >= 0.2.0
Requires:         R-CRAN-purrr 
Requires:         R-utils 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-globals 
Requires:         R-CRAN-prettyunits 

%description
A common interface is provided to allow users to specify a model without
having to remember the different argument names across different functions
or computational engines (e.g. 'R', 'Spark', 'Stan', etc).

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
