%global __brp_check_rpaths %{nil}
%global packname  nna
%global packver   0.0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Nearest-Neighbor Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch

%description
Calculates spatial pattern analysis using a T-square sample procedure.
This method is based on two measures "x" and "y". "x" - Distance from the
random point to the nearest individual. "y" - Distance from individual to
its nearest neighbor. This is a methodology commonly used in
phytosociology or marine benthos ecology to analyze the species'
distribution (random, uniform or clumped patterns). Ludwig & Reynolds
(1988, ISBN:0471832359).

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
