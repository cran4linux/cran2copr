%global packname  statar
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Tools Inspired by 'Stata' to Manipulate Tabular Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
A set of tools inspired by 'Stata' to explore data.frames ('summarize',
'tabulate', 'xtile', 'pctile', 'binscatter', elapsed quarters/month,
lead/lag).

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
