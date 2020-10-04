%global packname  webr
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}%{?buildtag}
Summary:          Data and Functions for Web-Based Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-moonBook 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sjlabelled 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rrtable 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ztable 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-vcd 
Requires:         R-CRAN-moonBook 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sjlabelled 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rrtable 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-psych 
Requires:         R-grid 
Requires:         R-CRAN-ztable 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-vcd 

%description
Several analysis-related functions for the book entitled "Web-based
Analysis without R in Your Computer"(written in Korean, ISBN
978-89-5566-185-9) by Keon-Woong Moon. The main function plot.htest()
shows the distribution of statistic for the object of class 'htest'.

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
