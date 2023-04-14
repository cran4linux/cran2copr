%global __brp_check_rpaths %{nil}
%global packname  poweRlaw
%global packver   0.70.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.70.6
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Heavy Tailed Distributions

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-utils 

%description
An implementation of maximum likelihood estimators for a variety of heavy
tailed distributions, including both the discrete and continuous power law
distributions. Additionally, a goodness-of-fit based approach is used to
estimate the lower cut-off for the scaling region.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
