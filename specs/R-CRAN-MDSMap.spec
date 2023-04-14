%global __brp_check_rpaths %{nil}
%global packname  MDSMap
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          High Density Genetic Linkage Mapping using MultidimensionalScaling

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-princurve >= 2.1.2
BuildRequires:    R-CRAN-smacof >= 1.9.0
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-princurve >= 2.1.2
Requires:         R-CRAN-smacof >= 1.9.0
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-reshape 

%description
Estimate genetic linkage maps for markers on a single chromosome (or in a
single linkage group) from pairwise recombination fractions or intermarker
distances using weighted metric multidimensional scaling. The methods are
suitable for autotetraploid as well as diploid populations. Options for
assessing the fit to a known map are also provided. Methods are discussed
in detail in Preedy and Hackett (2016) <doi:10.1007/s00122-016-2761-8>.

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
