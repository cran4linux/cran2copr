%global __brp_check_rpaths %{nil}
%global packname  GNSSseg
%global packver   6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0
Release:          3%{?dist}%{?buildtag}
Summary:          Homogenization of GNSS Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-capushe 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-capushe 

%description
Homogenize GNSS (Global Navigation Satellite System) time-series. The
general model is a segmentation in the mean model including a periodic
function and considering monthly variances, see Quarello (2020)
<arXiv:2005.04683>.

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
