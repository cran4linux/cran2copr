%global __brp_check_rpaths %{nil}
%global packname  ssmn
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Skew Scale Mixtures of Normal Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-sn 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-sn 

%description
Performs the EM algorithm for regression models using Skew Scale Mixtures
of Normal Distributions.

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
