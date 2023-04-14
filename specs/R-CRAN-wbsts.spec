%global __brp_check_rpaths %{nil}
%global packname  wbsts
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple Change-Point Detection for Nonstationary Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-wavelets 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-wavelets 

%description
Implements detection for the number and locations of the change-points in
a time series using the Wild Binary Segmentation and the Locally
Stationary Wavelet model of Korkas and Fryzlewicz (2017)
<doi:10.5705/ss.202015.0262>.

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
