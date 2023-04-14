%global __brp_check_rpaths %{nil}
%global packname  nlshrink
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Linear Shrinkage Estimation of Population Eigenvalues andCovariance Matrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-stats >= 3.2.3
BuildRequires:    R-graphics >= 3.2.3
BuildRequires:    R-CRAN-nloptr >= 1.0.4
Requires:         R-MASS >= 7.3.45
Requires:         R-stats >= 3.2.3
Requires:         R-graphics >= 3.2.3
Requires:         R-CRAN-nloptr >= 1.0.4

%description
Non-linear shrinkage estimation of population eigenvalues and covariance
matrices, based on publications by Ledoit and Wolf (2004, 2015, 2016).

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
