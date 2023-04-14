%global __brp_check_rpaths %{nil}
%global packname  fpop
%global packver   2019.08.26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.08.26
Release:          3%{?dist}%{?buildtag}
Summary:          Segmentation using Optimal Partitioning and Function Pruning

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
A dynamic programming algorithm for the fast segmentation of univariate
signals into piecewise constant profiles. The 'fpop' package is a wrapper
to a C++ implementation of the fpop (Functional Pruning Optimal
Partioning) algorithm described in Maidstone et al. 2017
<doi:10.1007/s11222-016-9636-3>. The problem of detecting changepoints in
an univariate sequence is formulated in terms of minimising the mean
squared error over segmentations. The fpop algorithm exactly minimizes the
mean squared error for a penalty linear in the number of changepoints.

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
