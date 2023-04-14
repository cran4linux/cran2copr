%global __brp_check_rpaths %{nil}
%global packname  clr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Curve Linear Regression via Dimension Reduction

License:          LGPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
A new methodology for linear regression with both curve response and curve
regressors, which is described in Cho, Goude, Brossat and Yao (2013)
<doi:10.1080/01621459.2012.722900> and (2015)
<doi:10.1007/978-3-319-18732-7_3>. The key idea behind this methodology is
dimension reduction based on a singular value decomposition in a Hilbert
space, which reduces the curve regression problem to several scalar linear
regression problems.

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
