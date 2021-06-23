%global __brp_check_rpaths %{nil}
%global packname  applicable
%global packver   0.0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Compilation of Applicability Domain Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-hardhat >= 0.1.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-proxyC 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-hardhat >= 0.1.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-proxyC 
Requires:         R-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 

%description
A modeling package compiling applicability domain methods in R. It
combines different methods to measure the amount of extrapolation new
samples can have from the training set. See Netzeva et al (2005)
<doi:10.1177/026119290503300209> for an overview of applicability domains.

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
