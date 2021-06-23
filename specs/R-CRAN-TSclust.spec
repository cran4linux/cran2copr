%global __brp_check_rpaths %{nil}
%global packname  TSclust
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Clustering Utilities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-pdc 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-locpol 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-longitudinalData 
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-pdc 
Requires:         R-cluster 
Requires:         R-CRAN-locpol 
Requires:         R-KernSmooth 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-longitudinalData 
Requires:         R-CRAN-forecast 

%description
A set of measures of dissimilarity between time series to perform time
series clustering. Metrics based on raw data, on generating models and on
the forecast behavior are implemented. Some additional utilities related
to time series clustering are also provided, such as clustering algorithms
and cluster evaluation metrics.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
