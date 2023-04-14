%global __brp_check_rpaths %{nil}
%global packname  jointMeanCov
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Joint Mean and Covariance Estimation for Matrix-Variate Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-glasso 
Requires:         R-graphics 
Requires:         R-stats 

%description
Jointly estimates two-group means and covariances for matrix-variate data
and calculates test statistics. This package implements the algorithms
defined in Hornstein, Fan, Shedden, and Zhou (2018)
<doi:10.1080/01621459.2018.1429275>.

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
