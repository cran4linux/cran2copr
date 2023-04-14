%global __brp_check_rpaths %{nil}
%global packname  ahnr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          An Implementation of the Artificial Hydrocarbon Networks

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-magrittr 

%description
Implementation of the Artificial Hydrocarbon Networks for data modeling.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
