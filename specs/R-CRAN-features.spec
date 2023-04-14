%global __brp_check_rpaths %{nil}
%global packname  features
%global packver   2015.12-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2015.12.1
Release:          3%{?dist}%{?buildtag}
Summary:          Feature Extraction for Discretely-Sampled Functional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lokern 
Requires:         R-CRAN-lokern 

%description
Discretely-sampled function is first smoothed.  Features of the smoothed
function are then extracted.  Some of the key features include mean value,
first and second derivatives, critical points (i.e. local maxima and
minima), curvature of cunction at critical points, wiggliness of the
function, noise in data, and outliers in data.

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
