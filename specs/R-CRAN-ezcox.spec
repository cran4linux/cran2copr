%global packname  ezcox
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          2%{?dist}
Summary:          Easily Process a Batch of Cox Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-forestmodel 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-survival 
Requires:         R-CRAN-forestmodel 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 

%description
A tool to operate a batch of univariate or multivariate Cox models and
return tidy result.

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
