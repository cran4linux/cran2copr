%global packname  dials
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Creating Tuning Parameter Values

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-vctrs >= 0.3.0.9000
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-DiceDesign 
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-vctrs >= 0.3.0.9000
Requires:         R-CRAN-scales 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-DiceDesign 

%description
Many models contain tuning parameters (i.e. parameters that cannot be
directly estimated from the data). These tools can be used to define
objects for creating, simulating, or validating values for such
parameters.

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
