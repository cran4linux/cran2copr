%global packname  tune
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Tidy Tuning Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-recipes >= 0.1.9
BuildRequires:    R-CRAN-workflows >= 0.1.0
BuildRequires:    R-CRAN-hardhat >= 0.1.0
BuildRequires:    R-CRAN-dials >= 0.0.4
BuildRequires:    R-CRAN-parsnip >= 0.0.4
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-GPfit 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-recipes >= 0.1.9
Requires:         R-CRAN-workflows >= 0.1.0
Requires:         R-CRAN-hardhat >= 0.1.0
Requires:         R-CRAN-dials >= 0.0.4
Requires:         R-CRAN-parsnip >= 0.0.4
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-GPfit 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-lifecycle 

%description
The ability to tune models is important. 'tune' contains functions and
classes to be used in conjunction with other 'tidymodels' packages for
finding reasonable values of hyper-parameters in models, pre-processing
methods, and post-processing steps.

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
