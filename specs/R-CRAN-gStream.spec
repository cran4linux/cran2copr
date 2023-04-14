%global __brp_check_rpaths %{nil}
%global packname  gStream
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Graph-Based Sequential Change-Point Detection for Streaming Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch

%description
Uses an approach based on k-nearest neighbor information to sequentially
detect change-points. Offers analytic approximations for false discovery
control given user-specified average run length.  Can be applied to any
type of data (high-dimensional, non-Euclidean, etc.) as long as a
reasonable similarity measure is available.  See references (1) Chen, H.
(2019) Sequential change-point detection based on nearest neighbors. The
Annals of Statistics, 47(3):1381-1407. (2) Chu, L. and Chen, H. (2018)
Sequential change-point detection for high-dimensional and non-Euclidean
data <arXiv:1810.05973>.

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
