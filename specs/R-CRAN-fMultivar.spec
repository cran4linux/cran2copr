%global __brp_check_rpaths %{nil}
%global packname  fMultivar
%global packver   3042.80.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3042.80.1
Release:          2%{?dist}%{?buildtag}
Summary:          Rmetrics - Analysing and Modeling Multivariate Financial ReturnDistributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sn 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides a collection of functions to manage, to investigate and to
analyze bivariate and multivariate data sets of financial returns.

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
