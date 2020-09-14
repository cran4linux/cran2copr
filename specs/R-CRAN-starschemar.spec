%global packname  starschemar
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Obtaining Star Schemas from Flat Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-generics 

%description
Data in multidimensional systems is obtained from operational systems and
is transformed to adapt it to the new structure. Frequently, the
operations to be performed aim to transform a flat table into a star
schema. Transformations can be carried out using professional ETL
(extract, transform and load) tools or tools intended for data
transformation for end users. With the tools mentioned, this
transformation can be carried out, but it requires a lot of work. The main
objective this package is to define transformations that allow obtaining
star schemas from flat tables easily. In addition, it includes basic data
cleaning, dimension enrichment, incremental data refresh and query
operations, adapted to this context.

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
