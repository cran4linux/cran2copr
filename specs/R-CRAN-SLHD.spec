%global __brp_check_rpaths %{nil}
%global packname  SLHD
%global packver   2.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Maximin-Distance (Sliced) Latin Hypercube Designs

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Generate the optimal Latin Hypercube Designs (LHDs) for computer
experiments with quantitative factors and the optimal Sliced Latin
Hypercube Designs (SLHDs) for computer experiments with both quantitative
and qualitative factors. Details of the algorithm can be found in Ba, S.,
Brenneman, W. A. and Myers, W. R. (2015), "Optimal Sliced Latin Hypercube
Designs," Technometrics. Important function in this package is
"maximinSLHD".

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
