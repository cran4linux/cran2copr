%global __brp_check_rpaths %{nil}
%global packname  teda
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          An Implementation of the Typicality and Eccentricity DataAnalysis Framework

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
The typicality and eccentricity data analysis (TEDA) framework was put
forward by Angelov (2013) <DOI:10.14313/JAMRIS_2-2014/16>. It has been
further developed into multiple different techniques since, and provides a
non-parametric way of determining how similar an observation, from a
process that is not purely random, is to other observations generated by
the process. This package provides code to use the batch and recursive
TEDA methods that have been published.

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
