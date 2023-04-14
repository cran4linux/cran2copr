%global __brp_check_rpaths %{nil}
%global packname  phylin
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Interpolation of Genetic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The spatial interpolation of genetic distances between samples is based on
a modified kriging method that accepts a genetic distance matrix and
generates a map of probability of lineage presence. This package also
offers tools to generate a map of potential contact zones between groups
with user-defined thresholds in the tree to account for old and recent
divergence. Additionally, it has functions for IDW interpolation using
genetic data and midpoints.

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
